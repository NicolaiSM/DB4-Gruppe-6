import _thread
import time
from src.API.cooler import Cooler
from src.API.feeder import Feeder
from src.Models.controlloop import Controlloop
from src.Models.localstorage import Localstorage
from src.Models.mqtt import Mqtt
from src.Models.pid import Pid
import math

#Cooler
cooler_pump_dir = 15
cooler_pump_step = 33

cooler_cool = 13
cooler_fan = 32
cooler_sensor = 36

#Feeder
feeder_pump_dir = 14
feeder_pump_step = 12
feeder_sensor = 34
feeder_led = 26

localstorage = Localstorage()
cooler = Cooler(cooler_fan, cooler_cool, cooler_pump_dir, cooler_pump_step, cooler_sensor, 50)
coolpid = Pid(755, 470, 425, 20, 18)
feed = Feeder(feeder_sensor, feeder_pump_dir, feeder_pump_step, feeder_led, 20)


mqttapi = {b'Dreambot/feeds/Peltier Element': cooler.setVoltage,
            b'Dreambot/feeds/Fan': cooler.setFan,
            b'Dreambot/feeds/P': coolpid.setp,
            b'Dreambot/feeds/I': coolpid.seti,
            b'Dreambot/feeds/D': coolpid.setd,
            }

#mqtt = Mqtt(mqttapi)


def coolfunc():
    cooler.speed(coolpid(cooler.measure()))


def feederfunc():
    ec = 3000  # cell/mL
    cl = 0.00029  # liters/s
    vf = 3000  # liters
    n = 2  # no. of mussels
    while True:
        sc = feed.measure()  # concentration in algae tank
        f = ec * vf / sc  # volume of algae juice dosis
        #t = math.log(ec / sc) * 1 / (-cl * n)  # time until next OD measurement
        print("ml" + str(f))
        feed.feed(f)
        time.sleep(10)

def localfunc():
    feedmes = feed.measure()
    coolmes = cooler.measure()
    localstorage(feedmes, coolmes)
    #print("OD " + str(feedmes))
    #print("temp " + str(coolmes))


#mqttloop = Controlloop(3, _thread.allocate_lock(), mqtt)
temppid = Controlloop(7, _thread.allocate_lock(), coolfunc)
#feedctl = Controlloop(7, _thread.allocate_lock(), feederfunc)
localloop = Controlloop(60, _thread.allocate_lock(), localfunc)

#_thread.start_new_thread(mqttloop, ())
_thread.start_new_thread(temppid, ())
_thread.start_new_thread(feederfunc, ())
_thread.start_new_thread(localloop, ())
