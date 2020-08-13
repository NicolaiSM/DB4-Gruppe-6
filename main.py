import _thread

from src.API.cooler import Cooler
from src.Models.controlloop import Controlloop
from src.Models.mqtt import Mqtt
from src.Models.pid import Pid

#Cooler



#Feeder




cooler = Cooler()
coolpid = Pid(1,1,1,10)


mqttapi = {b'Dreambot/feeds/Peltier Element': cooler.setVoltage,
            b'Dreambot/feeds/Fan': cooler.setFan,
            b'Dreambot/feeds/P': coolpid.setP,
            b'Dreambot/feeds/I': coolpid.setI,
            b'Dreambot/feeds/D': coolpid.setD,
            }

mqtt = Mqtt(mqttapi)


temppid = Controlloop(2, True, lambda x: cooler.speed(coolpid(cooler.measure())))

_thread.start_new_thread(mqtt, ())
_thread.start_new_thread(temppid, ())




