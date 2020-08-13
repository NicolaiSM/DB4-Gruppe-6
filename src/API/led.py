import machine


class Led:

    def __init__(self, pin, bits=12, write=255):
        self.bits = bits
        self.led = machine.DAC(machine.Pin(pin), bits=bits)
        self.led.write(write)

    def setbits(self, bits):
        self.led.init(bits=bits)

    def setLedV(self, value):
        self.led.write(value)
