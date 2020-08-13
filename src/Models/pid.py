import time

from src.API.feeder import Feeder
from src.Models.queue import Queue


class Pid(Queue):

    def __init__(self, p, i, d, size, target):
        Queue.__init__(self, size)
        self.p = p
        self.i = i
        self.d = d
        self.target = target

    def __call__(self, other):
        self.add(other-self.target)
        return self.p * self.last() + self.i * self.diff() + self.d * self.sum()

    def setP(self, p):
        self.p = float(p)

    def setI(self, i):
        self.i = float(i)

    def setD(self, d):
        self.d = float(d)







