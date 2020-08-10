import machine

class Pump():

    def __init__(self, pin1, pin2):
        self.dir = machine.Pin(pin1)
        self.control = machine.PWM(pin2)
        self.duty_on = 512
        self.duty_off = 0
        self.freqtorotation = 3200

    def forward(self, value):
        self.dir.on()
        self.duty(self.duty_on)

    def backward(self, value):
        self.dir.off()
        self.duty(self.duty_on)

    def off(self):
        self.duty(self.duty_off)

    def volume(self, value):
        pass

    def speed(self, value):
        self.freq(value*self.rotationtofreq)

