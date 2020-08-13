
class Queue:

    def __init__(self, size):
        self.list = []
        self.size = size

    def add(self, other):
        self.list.append(other)

        if len(self.list) > self.size:
            self.list.pop(0)

    def last(self):
        return self.list[-1]

    def sum(self):
        return sum(self.list)

    def diff(self):
        if len(self.list) == 1:
            return self.list[-1]
        else:
            return self.list[-2] - self.list[-1]


