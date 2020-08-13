import machine

from src.API.pump import Pump
from src.API.sensor import Sensor
from src.Models.tempconversion import voltagetempconv


class Cooler(Pump, Sensor):

    def __init__(self, pin1, pin2, pin3, pin4, pin5, nummes):
        Pump.__init__(self, pin3, pin4)
        Sensor.__init__(self, pin5, nummes, voltagetempconv)
        self.fan = machine.Pin(pin1, machine.Pin.OUT)
        self.cooler = machine.Pin(pin2, machine.Pin.OUT)
        self.fan_on()
        self.v12()


    def fan_on(self):
        self.fan.on()

    def fan_off(self):
        self.fan.off()

    def v5(self):
        self.cooler.on()

    def v12(self):
        self.cooler.off()

    # Peltier 5V or 12V
    def setVoltage(self, msg):
        if msg == '12V':
            self.v12()
        else:
            self.v5()

    # Fan on or off
    def setFan(self, msg):
        if msg == 'ON':
            self.fan_on()
        else:
            self.fan_off()




