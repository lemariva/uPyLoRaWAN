# The MIT License (MIT)
#
# Copyright (c) 2018 Brent Rubell for Adafruit
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`ttn_usa.py`
======================================================
The Things Network Frequency Plans - US902
* Author(s): Brent Rubell
"""
TTN_FREQS = {0: (0xE1, 0xF9, 0xC0), # 903.9 MHz
             1: (0xE2, 0x06, 0x8C), # 904.1 MHz
             2: (0xE2, 0x13, 0x20), # 904.3 MHz
             3: (0xE2, 0x20, 0x26), # 904.5 MHz
             4: (0xE2, 0x2C, 0xF3), # 904.7 MHz
             5: (0xE2, 0x39, 0xc0), # 904.9 MHz
             6: (0xE2, 0x46, 0x8c), # 905.1 MHz
             7: (0xE2, 0x53, 0x59)} # 905.3 MHz
