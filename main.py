import _thread
import time
from src.API.cooler import Cooler
from src.API.feeder import Feeder
from src.Models.controlloop import Controlloop
from src.Models.mqtt import Mqtt
from src.Models.pid import Pid

#Cooler
cooler_pump_dir = 33
cooler_pump_step = 15
cooler_cool = 13
cooler_fan = 14
cooler_sensor = 32

#Feeder
feeder_pump_dir = 27
feeder_pump_step = 12
feeder_sensor = 34
feeder_led = 26

cooler = Cooler(cooler_fan, cooler_cool, cooler_pump_dir, cooler_pump_step, cooler_sensor, 50)
coolpid = Pid(755, 220, 425, 20, 18)
feed = Feeder(34)


mqttapi = {b'Dreambot/feeds/Peltier Element': cooler.setVoltage,
            b'Dreambot/feeds/Fan': cooler.setFan,
            b'Dreambot/feeds/P': coolpid.setp,
            b'Dreambot/feeds/I': coolpid.seti,
            b'Dreambot/feeds/D': coolpid.setd,
            }

mqtt = Mqtt(mqttapi)


def coolfunc():
    return cooler.speed(mqtt.publish("RPM", coolpid(mqtt.publish("TempRead", cooler.measure()))))


def feederfunc():
    return None


mqttloop = Controlloop(3, _thread.allocate_lock(), mqtt)
temppid = Controlloop(7, _thread.allocate_lock(), coolfunc)
feedctl = Controlloop(7, _thread.allocate_lock(), feederfunc)

_thread.start_new_thread(mqttloop, ())
_thread.start_new_thread(temppid, ())
_thread.start_new_thread(feedctl, ())
