import machine
import math


class Sensor:

    def __init__(self, pin, nummes, model=None):
        # Setup ADC pin
        self.mes = []
        self.nummes = nummes
        self.adc = machine.ADC(machine.Pin(pin))
        self.adc.atten(machine.ADC.ATTN_11DB)
        self.adc.width(machine.ADC.WIDTH_10BIT)

        # Keep raw data if no model is provided
        if model is None:
            self.model = lambda x: x
        else:
            self.model = model

    # Get measurement and use model
    def measure(self):
        self.mes = []
        for i in range(self.nummes):
            self.mes.append(self.model(self.adc.read()))
        return sum(self.mes)/self.nummes

    def stde(self):
        self.mes = []
        for i in range(self.nummes):
            self.mes.append(self.model(self.adc.read()))
        avg = sum(self.mes)/self.nummes
        error = 0
        for i in range(self.nummes):
            error += (self.mes[i]-avg)**2
        return (math.sqrt(error/self.nummes))/math.sqrt(self.nummes)





