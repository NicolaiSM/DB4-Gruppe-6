import machine


class Pump2:

    def __init__(self, pin1, pin2):
        self.pwm = machine.PWM(machine.Pin(pin2))
        self.dir = machine.Pin(pin1, machine.Pin.OUT)
        self.duty_on = 1
        self.duty_off = 0

    def forward(self):
        self.dir.off()
        self.pwm.duty(self.duty_on)

    def backward(self):
        self.dir.on()
        self.pwm.duty(self.duty_on)

    def off(self):
        self.pwm.duty(self.duty_off)

    def volume(self, value):
        pass

    def speed(self, value):
        self.pwm.duty(self.duty_on)
        self.pwm.freq(int(value))
