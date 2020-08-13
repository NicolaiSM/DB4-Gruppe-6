import time


class Controlloop:

    def __init__(self, freq, l, func):
        self.freq = freq
        self.l = l
        self.k = 1
        self.func = func

    def __call__(self):
        while self.l:
            with self.l:
                self.func()
                time.sleep(self.freq)

    def setfreq(self, freq):
        self.freq = freq
