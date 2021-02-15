# uPyLoraWAN
The ESP32, Raspberry PI Pico, and M5Stack using MicroPython meet LoRaWAN.

Check out these articles for more information:
* [M5Stack Atom Matrix: LoRaWAN node running MicroPython](https://lemariva.com/blog/2020/03/m5stack-atom-lorawan-node-running-micropython)
* [Tutorial: ESP32 running MicroPython sends data over LoRaWAN](https://lemariva.com/blog/2020/02/tutorial-micropython-esp32-sends-data-over-lorawan)
* [Raspberry Pi Pico: The RP2040 meets LoRaWAN](https://lemariva.com/blog/2021/02/raspberry-pi-pico-rp2040-meets-lorawan)

:warning: Nowadays (20210215) you need to extend the MicroPython version to include support for encryption. To do that, check out [this tutorial](https://lemariva.com/blog/2021/02/raspberry-pi-pico-rp2040-meets-lorawan), and this repository [lemariva/micropython-pico-mbedtls](https://github.com/lemariva/micropython-pico-mbedtls).

# Video

[![M5Stack Atom Matrix running MicroPython meets LoRaWAN](https://img.youtube.com/vi/Nu60jVDbLW8/0.jpg)](https://www.youtube.com/watch?v=Nu60jVDbLW8)

# Setup
Use [VSCode and the PyMakr extension](https://lemariva.com/blog/2018/12/micropython-visual-studio-code-as-ide) to upload the code. If you are new on MicroPython, [this tutorial](https://lemariva.com/blog/2017/10/micropython-getting-started) can help you to install the firmware on a ESP32.

Follow these steps to deploy the project:

1. Rename the file `config.sample.py` to `config.py`
2. Configure the SPI pins to connect to the SX127x module. I've included the following example connections:
    * [ES32 TTGO v1.0](https://www.banggood.com/custlink/v3KmwRD2tf)
    * [M5Stack ATOM](https://www.banggood.com/custlink/KK331YvU8K) connected to [LoRa v2.0 board](https://s.click.aliexpress.com/e/_dU6udTr).
    * [M5Stack Fire](https://www.banggood.com/custlink/DvKKuhvU9J) connected to the [LoRa868 Module](https://www.banggood.com/custlink/DGvGud3zSI).
    * [Raspberry Pi Pico](https://www.raspberrypi.org/products/raspberry-pi-pico/) connected to [LoRa v2.0 board](https://s.click.aliexpress.com/e/_dU6udTr).
3. Configure the `devaddr`, `nwkey`, and `app` of the `ttn_config` variable following the instruction from [this link](https://lemariva.com/blog/2020/03/m5stack-atom-lorawan-node-running-micropython).

# Hardware
* [Wemos® TTGO LORA32 868/915Mhz](https://www.banggood.com/2Pcs-Wemos-TTGO-LORA32-868915Mhz-ESP32-LoRa-OLED-0_96-Inch-Blue-Display-p-1239769.html?p=QW0903761303201409LG) board.
* [SparkFun® LoRa Gateway - 1-Channel](https://www.sparkfun.com/products/15006) board.
* [M5Stack ATOM](https://www.banggood.com/custlink/KmGDkSGLhO) connected to [LoRa v2.0 board](https://s.click.aliexpress.com/e/_dU6udTr).
[M5Stack Fire](https://www.banggood.com/custlink/DvKKuhvU9J) connected to the [LoRa868 Module](https://www.banggood.com/custlink/DGvGud3zSI).

# Revision
* 0.2v - first commit with LoRaWAN support

# Licenses
* Apache 2.0

# Results
Two screenshots from the TTN website:
![application data](images/application_micropython.png)
![gateway traffic](images/gateway_traffic.png)

# References
* SX127x driver is based on: [Wei1234c GitHub](https://github.com/Wei1234c/SX127x_driver_for_MicroPython_on_ESP8266). The project was cleaned and made compatible with the [Wemos® TTGO LORA32 868/915Mhz](https://www.banggood.com/2Pcs-Wemos-TTGO-LORA32-868915Mhz-ESP32-LoRa-OLED-0_96-Inch-Blue-Display-p-1239769.html?p=QW0903761303201409LG) board.
* LoRaWAN connection is based on: [Adafruit_CircuitPython_TinyLoRa](https://github.com/adafruit/Adafruit_CircuitPython_TinyLoRa)
