import utime
import struct
import urandom
from sx127x import TTN, SX127x
from machine import Pin, SPI
from ttn_config import *


__DEBUG__ = True


ttn_config = TTN(DEVADDR, NWKEY, APP, country="EU")
device_pins = {
    'miso':19,
    'mosi':27,
    'ss':18,
    'sck':5,
    'dio_0':26,
    'reset':16,
    'led':2, 
}

device_spi = SPI(baudrate = 10000000, 
        polarity = 0, phase = 0, bits = 8, firstbit = SPI.MSB,
        sck = Pin(device_pins['sck'], Pin.OUT, Pin.PULL_DOWN),
        mosi = Pin(device_pins['mosi'], Pin.OUT, Pin.PULL_UP),
        miso = Pin(device_pins['miso'], Pin.IN, Pin.PULL_UP))

lora = SX127x(device_spi, pins=device_pins, ttn_config=ttn_config)


frame_counter = 0
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
    
    frame_counter += 1
    utime.sleep_ms(10000)