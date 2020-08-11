import time

class Pid():

    def __init__(self, p, i, d, target, freq):
        self.p = p
        self.i = i
        self.d = d
        self.target = target
        self.freq = freq

    def __call__(self):
        return self.p * data.last() + self.i * data.diff() + self.d * data.sum(self.target)

    def func(self):

        while True÷

            time.sleep(self.freq)





