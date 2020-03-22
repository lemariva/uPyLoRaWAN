# AES-Python, Copyright (C) 2012 Bo Zhu http://about.bozhu.me
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#
# Modified by Brent Rubell for Adafruit Industries
# Modified by Mauro Riva for LeMaRiva|Tech

from ucryptolib import aes

class AES:
    
    def __init__(self, device_address, app_key, network_key, frame_counter):
        self._app_key = app_key
        self._device_address = device_address
        self._network_key = network_key
        self.frame_counter = frame_counter

    def encrypt(self, aes_data):
        """Performs AES Encryption routine with data.
        :param bytearray data: Data to-be encrypted.
        """
        self.encrypt_payload(aes_data)
        return aes_data

    def decrypt_payload(self, cipher):
        _aes = aes(self._app_key, 1)
        print(cipher)
        return cipher

    def encrypt_payload(self, data):
        """Encrypts data payload.
        :param bytearray data: Data to-be-encrypted.
        """
        _aes = aes(self._app_key, 1)

        block_a = bytearray(16)
        # calculate required number of blocks
        num_blocks = len(data) // 16
        incomplete_block_size = len(data) % 16
        if incomplete_block_size != 0:
            num_blocks += 1
        # k = data ptr
        k = 0
        i = 1
        while i <= num_blocks:
            block_a[0] = 0x01
            block_a[1] = 0x00
            block_a[2] = 0x00
            block_a[3] = 0x00
            block_a[4] = 0x00
            block_a[5] = 0x00
            # block from device_address, MSB first
            block_a[6] = self._device_address[3]
            block_a[7] = self._device_address[2]
            block_a[8] = self._device_address[1]
            block_a[9] = self._device_address[0]
            # block from frame counter
            block_a[10] = self.frame_counter & 0x00FF
            block_a[11] = (self.frame_counter >> 8) & 0x00FF
            block_a[12] = 0x00
            block_a[13] = 0x00
            block_a[14] = 0x00
            block_a[15] = i
            # calculate S
            #self._aes_encrypt(block_a, self._app_key)
            block_a = bytearray(_aes.encrypt(block_a))
            # check for last block
            if i != num_blocks:
                for j in range(16):
                    data[k] ^= block_a[j]
                    k += 1
            else:
                if incomplete_block_size == 0:
                    incomplete_block_size = 16
                for j in range(incomplete_block_size):
                    data[k] ^= block_a[j]
                    k += 1
            i += 1


    def calculate_mic(self, lora_packet, lora_packet_length, mic):
        """Calculates the validity of data messages, generates a message integrity check bytearray.
        """
        _aes = aes(self._network_key, 1)
        block_b = bytearray(16)
        key_k1 = bytearray(16)
        key_k2 = bytearray(16)
        old_data = bytearray(16)
        new_data = bytearray(16)
        block_b[0] = 0x49
        block_b[6] = self._device_address[3]
        block_b[7] = self._device_address[2]
        block_b[8] = self._device_address[1]
        block_b[9] = self._device_address[0]
        block_b[10] = self.frame_counter & 0x00FF
        block_b[11] = (self.frame_counter >> 8) & 0x00FF
        block_b[15] = lora_packet_length
        # calculate num. of blocks and blocksz of last block
        num_blocks = lora_packet_length // 16
        incomplete_block_size = lora_packet_length % 16
        if incomplete_block_size != 0:
            num_blocks += 1
        # generate keys
        self._mic_generate_keys(key_k1, key_k2)
        # aes encryption on block_b
        block_b = bytearray(_aes.encrypt(block_b))

        # copy block_b to old_data
        for i in range(16):
            old_data[i] = block_b[i]
        block_counter = 1
        # calculate until n-1 packet blocks
        k = 0  # ptr
        while block_counter < num_blocks:
            # copy data into array
            for i in range(16):
                new_data[i] = lora_packet[k]
                k += 1
            # XOR new_data with old_data
            self._xor_data(new_data, old_data)
            # aes encrypt new_data
            new_data = bytearray(_aes.encrypt(new_data))
            # copy new_data to old_data
            for i in range(16):
                old_data[i] = new_data[i]
            # increase block_counter
            block_counter += 1
        # perform calculation on last block
        if incomplete_block_size == 0:
            for i in range(16):
                new_data[i] = lora_packet[k]
                k += 1
            # xor with key 1
            self._xor_data(new_data, key_k1)
            # xor with old data
            self._xor_data(new_data, old_data)
            # aes routine
            new_data = bytearray(_aes.encrypt(new_data))
        else:
            # copy the remaining data
            for i in range(16):
                if i < incomplete_block_size:
                    new_data[i] = lora_packet[k]
                    k += 1
                if i == incomplete_block_size:
                    new_data[i] = 0x80
                if i > incomplete_block_size:
                    new_data[i] = 0x00
            # perform xor with key 2
            self._xor_data(new_data, key_k2)
            # perform xor with old data
            self._xor_data(new_data, old_data)
            new_data = bytearray(_aes.encrypt(new_data))
        # load MIC[] with data
        mic[0] = new_data[0]
        mic[1] = new_data[1]
        mic[2] = new_data[2]
        mic[3] = new_data[3]
        # return message integrity check array to calling method
        return mic

    def _mic_generate_keys(self, key_1, key_2):
        # encrypt the 0's in k1 with network key
        _aes = aes(self._network_key, 1)
        key_1 = bytearray(_aes.encrypt(key_1))
        # perform gen_key on key_1
        # check if key_1's msb is 1
        msb_key = (key_1[0] & 0x80) == 0x80
        # shift k1 left 1b
        self._shift_left(key_1)
        # check if msb is 1
        if msb_key:
            key_1[15] ^= 0x87
        # perform gen_key on key_2
        # copy key_1 to key_2
        key_2[0:16] = key_1[0:16]
        msb_key = (key_2[0] & 0x80) == 0x80
        self._shift_left(key_2)
        # check if msb is 1
        if msb_key:
            key_2[15] ^= 0x87

    @staticmethod
    def _shift_left(data):
        """ Shifts data bytearray left by 1
        """
        for i in range(16):
            if i < 15:
                if (data[i + 1] & 0x80) == 0x80:
                    overflow = 1
                else:
                    overflow = 0
            else:
                overflow = 0
            # shift 1b left
            data[i] = ((data[i] << 1) + overflow) & 0xFF

    @staticmethod
    def _xor_data(new_data, old_data):
        """ XOR two data arrays
        :param bytearray new_data: Calculated data.
        :param bytearray old_data: data to be xor'd.
        """
        for i in range(16):
            new_data[i] ^= old_data[i]