#import LoRaDuplexCallback
import LoRaPingPong
#import LoRaSender
#import LoRaReceiver
import config_lora
from sx127x import SX127x
from controller_esp32 import ESP32Controller


controller = ESP32Controller()
lora = controller.add_transceiver(SX127x(name = 'LoRa'),
                                  pin_id_ss = ESP32Controller.PIN_ID_FOR_LORA_SS,
                                  pin_id_RxDone = ESP32Controller.PIN_ID_FOR_LORA_DIO0)



#LoRaDuplexCallback.duplexCallback(lora)
LoRaPingPong.ping_pong(lora)
#LoRaSender.send(lora)
#LoRaReceiver.receive(lora)
