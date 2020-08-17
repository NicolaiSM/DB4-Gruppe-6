import time

from src.API.feeder import Feeder
from src.Models.queue import Queue


class Pid(Queue):

    def __init__(self, p, i, d, size, target):
        Queue.__init__(self, size)
        self.pid = {"p": p, "i": i, "d": d}
        self.target = target

    def __call__(self, other):
        error = other-self.target
        self.add(error)
        print(self.pid)
        print("ERROR" + str(error))
        y = self.pid["p"] * self.last() + self.pid["i"] * self.sum() + self.pid["d"] * self.diff()

        print("freq" + str(y))

        if y>=29000:
            return 29000

        return y

    def setp(self, p):
        self.pid["p"] = float(p)

    def seti(self, i):
        self.pid["i"] = float(i)

    def setd(self, d):
        self.pid["d"] = float(d)

    def settarget(self, target):
        self.target = float(target)
