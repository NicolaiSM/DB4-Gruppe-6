import utime


class Localstorage:

    def __init__(self):
        pass

    def __call__(self, temp, od):
        f = open('storage.txt', 'a+')
        # Temp, Time, OD.
        f.write(str(temp) + ',')
        f.write(str(utime.ticks_ms()) + ',')
        f.write(str(od) + ',')
        f.write('\n')
        f.close()