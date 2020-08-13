import time
import _thread

from src.API.cooler import Cooler
from src.API.sensor import Sensor
from src.Models.queue import Queue
from src.Models.pid import Pid

# Cooler pins
fan_pin = 14
cooler_pin = 13
cool_pump_dir = 27
cool_pump_step = 12
temp_sensor_pin = 32

# Feeder pins
feeder_pump_dir = 33
feeder_pump_step = 15


cooler = Cooler(fan_pin, cooler_pin, cool_pump_dir, cool_pump_step, temp_sensor_pin, 10)
pid = Pid(30, 30, 30, 10, 15)


class Tempcontrol:

    def __init__(self, freq, l):
        self.freq = freq
        self.l = l
        self.k = 1

    def __call__(self):
        while self.l:
            with self.l:
                temperature = cooler.measure()
                print(temperature)

                y = pid(temperature)

                print(y)

                cooler.speed(int(y))

                time.sleep(self.freq)

    def setfreq(self, freq):
        self.freq = freq


t = tempcontrol(3, _thread.allocate_lock())
_thread.start_new_thread(t, ())