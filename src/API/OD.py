from src.API.led import Led
from src.API.sensor import Sensor


class OD(Led, Sensor):

    def __init__(self, pin1, pin2, nummes):
        Led.__init__(self, pin1)
        Sensor.__init__(self, pin2, nummes)

