import machine

from src.API.pump import Pump


class Cooler(Pump):

    def __init__(self, pin1, pin2, pin3, pin4):
        self.fan = machine.Pin(pin1, machine.Pin.OUT)
        self.cooler = machine.Pin(pin2, machine.Pin.OUT)
        Pump.__init__(pin3, pin4)

    def fan_on(self):
        self.fan.on()

    def fan_off(self):
        self.fan.off()

    def v5(self):
        self.cooler.on()

    def v12(self):
        self.cooler.off()

