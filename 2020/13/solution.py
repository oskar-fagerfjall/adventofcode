""" placeholder doctring """
# I started with using the modulo as the arrives in time, but that is wrong.
# for bus 3 we want the arrival times to look like:
#  [0, 2, 1, 0, 2, 1]
# modulo gives             [0, 1, 2, 0, 1, 2]
# diff with (3-1):         [2, 1, 0, 2, 1, 0]
# and start at time (3-1): [0, 2, 1, 0, 2, 1] <-bingo!

def arrival(bus, time):
    """ placeholder doctring """
    return (bus-1) - ((time+bus-1) % bus)

def ontime(bus, time, expected):
    """ placeholder doctring """
    return arrival(bus, time) == expected

def allontime(arrivesafter, time):
    """ placeholder doctring """
    for bus, expected in arrivesafter.items():
        if not ontime(bus, time, expected):
            return False
    return True


# if __name__ == '__main__'