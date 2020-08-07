import machine

class Feeder(Lightsensor,Pump):

    def __init__(self):
        Lightsensor().__init__()
        Pump().__init__()

    def algaeMeasure(self):
        self.forward(x)
        self.measure()
        self.backward(x)

    def musselMeasure(self):
        self.backward(x)
        self.measure()
        self.forward(x)

    def feed(self,value):
        self.forward(value)