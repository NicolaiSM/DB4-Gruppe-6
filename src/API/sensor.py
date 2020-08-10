import machine


class Sensor:

    def __init__(self, pin, model=None):
        # Setup ADC pin
        self.adc = machine.ADC(pin)
        self.adc.atten(machine.ADC.ATTN_11DB)
        self.adc.width(machine.ADC.WIDTH_10BIT)

        # Keep raw data if no model is provided
        if model is None:
            self.model = lambda x: x
        else:
            self.model = model

    # Get measurement and use model
    def measure(self):
        return self.model(self.adc.read())
