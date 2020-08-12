import time

from src.API.feeder import Feeder
from src.Models.datastorage import Queue


class Pid:

    def __init__(self, p, i, d, target):
        self.p = p
        self.i = i
        self.d = d

    def __call__(self):
        return self.p * self.last() + self.i * self.diff() + self.d * self.sum()

    def setP(self, p):
        self.p = p

    def setI(self, i):
        self.i = i

    def setD(self, d):
        self.d = d




