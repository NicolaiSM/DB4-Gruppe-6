import machine


class Switch(machine.Pin):

    def __init__(self, pin1):
        super().__init__(pin1, machine.Pin.OUT)

    def on(self):
        super().on()

    def off(self):
        super().off()



