import utime
import struct
import urandom
from sx127x import TTN, SX127x
from machine import Pin, SPI
from ttn_config import *

# M5Stack
import neopixel
from letters import characters

__DEBUG__ = True

ttn_config = TTN(DEVADDR, NWKEY, APP, country="EU")

# M5Stack ATOM Matrix
device_pins = {
    'miso':23,
    'mosi':19,
    'ss':22,
    'sck':33,
    'dio_0':25,
    'reset':21,
    'led':12, 
}
"""
# ES32 TTGO v1.0 
device_pins = {
    'miso':19,
    'mosi':27,
    'ss':18,
    'sck':5,
    'dio_0':26,
    'reset':16,
    'led':2, 
}
"""
device_spi = SPI(baudrate = 10000000, 
        polarity = 0, phase = 0, bits = 8, firstbit = SPI.MSB,
        sck = Pin(device_pins['sck'], Pin.OUT, Pin.PULL_DOWN),
        mosi = Pin(device_pins['mosi'], Pin.OUT, Pin.PULL_UP),
        miso = Pin(device_pins['miso'], Pin.IN, Pin.PULL_UP))

lora = SX127x(device_spi, pins=device_pins, ttn_config=ttn_config)
frame_counter = 0

# M5Stack ATOM Matrix
text = "SOLIDARITY"
np = neopixel.NeoPixel(Pin(27), 25)

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

def on_receive(lora, outgoing):
    payload = lora.read_payload()
    print(payload)

lora.on_receive(on_receive)
lora.receive()

while True:
    epoch = utime.time()
    temperature = urandom.randint(0,30)

    payload = struct.pack('@Qh', int(epoch), int(temperature))

    if __DEBUG__:
        print("%s: %s" % (epoch, temperature))
        print(payload)

    lora.send_data(data=payload, data_length=len(payload), frame_counter=frame_counter)
    lora.receive()
    
    frame_counter += 1
    
    #M5Stack 
    for letter in text:
        char_to_leds(letter, (20, 20, 20))
        utime.sleep_ms(600)
    char_to_leds("!", (50, 5, 0))


    for i in range(200):
        utime.sleep_ms(100)