import utime
import struct
import urandom
from sx127x import TTN, SX127x
from machine import Pin, SPI
from ttn_config import *
import neopixel
from letters import characters

__DEBUG__ = True


ttn_config = TTN(DEVADDR, NWKEY, APP, country="EU")
device_pins = {
    'miso':23,
    'mosi':19,
    'ss':22,
    'sck':33,
    'dio_0':25,
    'reset':21,
    'led':27, 
}

device_spi = SPI(baudrate = 10000000, 
        polarity = 0, phase = 0, bits = 8, firstbit = SPI.MSB,
        sck = Pin(device_pins['sck'], Pin.OUT, Pin.PULL_DOWN),
        mosi = Pin(device_pins['mosi'], Pin.OUT, Pin.PULL_UP),
        miso = Pin(device_pins['miso'], Pin.IN, Pin.PULL_UP))

lora = SX127x(device_spi, pins=device_pins, ttn_config=ttn_config)
np = neopixel.NeoPixel(Pin(27), 25)

frame_counter = 0

text = "SOLIDARITY"

def char_to_leds(letter, color):
    rgb = color
    char_matrix = characters.get(letter)
    led_counter = 0
    for row in char_matrix:
        for led in row:
            if(led):
                np[led_counter] = rgb
            else:
                np[led_counter] = (0, 0, 0)
            led_counter += 1
    np.write()

while True:
    timestamp = utime.localtime()

    time_value = '%02d%02d%02d' %(timestamp[4], timestamp[5], timestamp[6])
    date_value = '%4d%02d%02d' %(timestamp[0], timestamp[1], timestamp[2])
    temperature = urandom.randint(0,30)
    
    payload = struct.pack('@qqh', int(date_value), int(time_value), int(temperature))

    if __DEBUG__:
        print(payload)
        print("%s %s: %s" % (date_value, time_value, temperature))
    
    lora.send_data(data=payload, data_length=len(payload), frame_counter=frame_counter)
    
    """
    if lora.received_packet():
        lora.blink_led()
        print('something here')
        payload = lora.read_payload()
        print(payload)
    """

    for letter in text:
        char_to_leds(letter, (20, 20, 20))
        utime.sleep_ms(600)
    char_to_leds("!", (50, 5, 0))

    frame_counter += 1
    utime.sleep_ms(5000)