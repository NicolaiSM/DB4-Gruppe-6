import machine
import time


class Pump:

    def __init__(self, pin1, pin2):
        self.pwm = machine.PWM(machine.Pin(pin2))
        self.dir = machine.Pin(pin1, machine.Pin.OUT)
        self.pin = machine.Pin(pin2, machine.Pin.OUT)
        self.duty_on = 1
        self.duty_off = 0

    def forward(self):
        self.dir.on()
        self.pwm.duty(self.duty_on)

    def backward(self):
        self.dir.off()
        self.pwm.duty(self.duty_on)

    def off(self):
        self.pwm.duty(self.duty_off)

    def volume(self, value):
        pass

    def speed(self, value):
        self.pwm.freq(int(value))

    def revs(self, revs):
        for j in range(revs):
            print(j)
            for i in range(3200):
                print(i)
                self.pin.on()
                self.pin.off()
                time.sleep(1 / 3200)
