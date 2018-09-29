from uPySensors.ssd1306_i2c import Display

def receive(lora):
    print("LoRa Receiver")
    display = Display()

    while True:
        if lora.receivedPacket():
            lora.blink_led()

            try:
                payload = lora.read_payload()
                display.show_text_wrap("{0} RSSI: {1}".format(payload.decode(), lora.packetRssi()))
                #print("*** Received message ***\n{}".format(payload.decode()))

            except Exception as e:
                print(e)
            #display.show_text("RSSI: {}\n".format(lora.packetRssi()), 10, 10)
            #print("with RSSI: {}\n".format(lora.packetRssi))
