import machine

from src.API.pump import Pump
from src.API.sensor import Sensor


class Feeder(Sensor, Pump):

    def __init__(self, pin1, pin2, pin3, nummes):
        Sensor.__init__(pin1, nummes)
        Pump.__init__(pin2, pin3)
        self.bvd = 0

    def algaeMeasure(self):
        self.forward(self.bvd)
        self.measure()
        self.backward(self.bvd)

    def musselMeasure(self):
        self.backward(self.bvd)
        self.measure()
        self.forward(self.bvd)

    def feed(self, value):
        self.forward(value)