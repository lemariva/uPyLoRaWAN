import utime
import struct
import urandom
from sx127x import TTN, SX127x
from machine import Pin, SPI
from config import *

# M5Stack
import neopixel
from letters import characters

__DEBUG__ = True

ttn_config = TTN(ttn_config['devaddr'], ttn_config['nwkey'], ttn_config['app'], country=ttn_config['country'])

device_spi = SPI(baudrate = 10000000, 
        polarity = 0, phase = 0, bits = 8, firstbit = SPI.MSB,
        sck = Pin(device_config['sck'], Pin.OUT, Pin.PULL_DOWN),
        mosi = Pin(device_config['mosi'], Pin.OUT, Pin.PULL_UP),
        miso = Pin(device_config['miso'], Pin.IN, Pin.PULL_UP))

lora = SX127x(device_spi, pins=device_config, lora_parameters=lora_parameters, ttn_config=ttn_config)
frame_counter = 0

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

    for i in range(app_config['loop']):
        utime.sleep_ms(app_config['sleep'])