import time
import config_lora


msgCount = 0            # count of outgoing messages
INTERVAL = 2000         # interval between sends
INTERVAL_BASE = 2000    # interval between sends base


def duplexCallback(lora):
    print("LoRa Duplex with callback")
    lora.onReceive(on_receive)  # register the receive callback
    do_loop(lora)


def do_loop(lora):
    global msgCount

    lastSendTime = 0
    interval = 0

    while True:
        now = config_lora.get_millis()

        if (now - lastSendTime > interval):
            lastSendTime = now                                      # timestamp the message
            interval = (lastSendTime % INTERVAL) + INTERVAL_BASE    # 2-3 seconds

            message = "{} {}".format(config_lora.get_nodename(), msgCount)
            print(interval, 'interval')
            sendMessage(lora, message)                              # send message
            msgCount += 1

            lora.receive()                                          # go into receive mode


def sendMessage(lora, outgoing):
    lora.println(outgoing)
    # print("Sending message:\n{}\n".format(outgoing))


def on_receive(lora, payload):
    lora.blink_led()

    try:
        payload_string = payload.decode()
        rssi = lora.packetRssi()
        print("*** Received message ***\n{}".format(payload_string))
    except Exception as e:
        print(e)
    print("with RSSI {}\n".format(rssi))
