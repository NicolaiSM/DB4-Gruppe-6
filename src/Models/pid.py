

class Error:

    def __init__(self):
        self.list = []

    def last(self):
        return self.list[len(self.list)]

    def diff(self):
        pass

    def sum(self, interval):
        pass


class Pid:

    def __init__(self, p, i, d, interval):
        self.p = p
        self.i = i
        self.d = d
        self.interval = interval

    def __call__(self, error):
        return self.p * error.last() + self.i * error.diff() + self.d * error.sum(self.interval)



