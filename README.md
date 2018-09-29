# uPyLora
ESP32 using MicroPython meets lora.

# Setup
* `LoRaPingPong.py`: sends ping-pong messages between the nodes (bidirectional communication)
* `LoRaReceiver.py` and `LoraSender.py`: unidirectional communication between the nodes (Note: deploy the `LoRaReceiver.py` on one node and the `LoraSender.py` on another node)

# Hardware
* (https://www.banggood.com/2Pcs-Wemos-TTGO-LORA32-868915Mhz-ESP32-LoRa-OLED-0_96-Inch-Blue-Display-p-1239769.html?p=QW0903761303201409LG)[Wemos® TTGO LORA32 868/915Mhz] board.

# Revision
* 0.1 first commit

# Licenses
* Apache 2.0

# References
* Basically based on: (https://github.com/Wei1234c/SX127x_driver_for_MicroPython_on_ESP8266)[Wei1234c GitHub]. The original project was cleaned and made compatible with the (https://www.banggood.com/2Pcs-Wemos-TTGO-LORA32-868915Mhz-ESP32-LoRa-OLED-0_96-Inch-Blue-Display-p-1239769.html?p=QW0903761303201409LG)[Wemos® TTGO LORA32 868/915Mhz] board.
