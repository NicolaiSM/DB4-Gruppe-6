
class Queue(list):

    def __init__(self, size):
        list.__init__([])

        # Max size of list
        self.size = size

    # Add value to queue
    def add(self, other):
        self.append(other)

        if len(self) > self.size:
            self.pop(0)


class Datastorage(dict):

    def __init__(self):
        dict.__init__({})

    # Add measurement to storage and create a new queue if new measurement
    def __add__(self, other):
        key, value = other
        if not key == self.keys():
            self[key] = Queue(other[2])

        self[key].append(value)
