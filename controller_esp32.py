from machine import Pin, SPI, reset
from controller import Controller


class ESP32Controller(Controller):

    # LoRa config
    PIN_ID_FOR_LORA_RESET = 14

    PIN_ID_FOR_LORA_SS = 18
    PIN_ID_SCK = 5
    PIN_ID_MOSI = 27
    PIN_ID_MISO = 19

    PIN_ID_FOR_LORA_DIO0 = 5
    PIN_ID_FOR_LORA_DIO1 = None
    PIN_ID_FOR_LORA_DIO2 = None
    PIN_ID_FOR_LORA_DIO3 = None
    PIN_ID_FOR_LORA_DIO4 = None
    PIN_ID_FOR_LORA_DIO5 = None


    # ESP config
    ON_BOARD_LED_PIN_NO = 2
    ON_BOARD_LED_HIGH_IS_ON = True
    GPIO_PINS = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                 12, 13, 14, 15, 16, 17, 18, 19, 21, 22,
                 23, 25, 26, 27, 32, 34, 35, 36, 37, 38, 39)


    def __init__(self,
                 pin_id_led = ON_BOARD_LED_PIN_NO,
                 on_board_led_high_is_on = ON_BOARD_LED_HIGH_IS_ON,
                 pin_id_reset = PIN_ID_FOR_LORA_RESET,
                 blink_on_start = (2, 0.5, 0.5)):

        super().__init__(pin_id_led,
                         on_board_led_high_is_on,
                         pin_id_reset,
                         blink_on_start)


    def prepare_pin(self, pin_id, in_out = Pin.OUT):
        if pin_id is not None:
            pin = Pin(pin_id, in_out)
            new_pin = Controller.Mock()
            new_pin.pin_id = pin_id
            new_pin.value = pin.value

            if in_out == Pin.OUT:
                new_pin.low = lambda : pin.value(0)
                new_pin.high = lambda : pin.value(1)
            else:
                new_pin.irq = pin.irq

            return new_pin


    def prepare_irq_pin(self, pin_id):
        pin = self.prepare_pin(pin_id, Pin.IN)
        if pin:
            pin.set_handler_for_irq_on_rising_edge = lambda handler: pin.irq(handler = handler, trigger = Pin.IRQ_RISING)
            pin.detach_irq = lambda : pin.irq(handler = None, trigger = 0)
            return pin


    def get_spi(self):
        spi = None

        try:
            spi = SPI(baudrate = 10000000, polarity = 0, phase = 0, bits = 8, firstbit = SPI.MSB,
                      sck = Pin(self.PIN_ID_SCK, Pin.OUT, Pin.PULL_DOWN),
                      mosi = Pin(self.PIN_ID_MOSI, Pin.OUT, Pin.PULL_UP),
                      miso = Pin(self.PIN_ID_MISO, Pin.IN, Pin.PULL_UP))
            #spi.init()

        except Exception as e:
            print(e)
            if spi:
                spi.deinit()
                spi = None
            reset()  # in case SPI is already in use, need to reset.

        return spi


    def prepare_spi(self, spi):

        if spi:
            new_spi = Controller.Mock()

            def transfer(pin_ss, address, value = 0x00):
                response = bytearray(1)

                pin_ss.low()

                spi.write(bytes([address]))
                spi.write_readinto(bytes([value]), response)

                pin_ss.high()

                return response

            new_spi.transfer = transfer
            new_spi.close = spi.deinit
            return new_spi


    def __exit__(self):
        self.spi.close()
