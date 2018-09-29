from time import sleep
from uPySensors.ssd1306_i2c import Display

def send(lora):
    counter = 0
    print("LoRa Sender")
    display = Display()

    while True:
        payload = 'Hello ({0})'.format(counter)
        #print("Sending packet: \n{}\n".format(payload))
        display.show_text_wrap("{0} RSSI: {1}".format(payload, lora.packetRssi()))
        lora.println(payload)

        counter += 1
        sleep(5)
