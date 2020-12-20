class Waypoint:
    pass

class Ship:
    def __init__( self ):
        self.x = 0
        self.y = 0
        self.wp = Waypoint()
        self.wp.x = 10
        self.wp.y = 1
    def north(self, dist):
        self.wp.y += dist
    def south(self, dist):
        self.wp.y -= dist
    def east(self, dist):
        self.wp.x += dist
    def west( self, dist):
        self.wp.x -= dist
    def right90(self):
        wpx = self.wp.x
        wpy = self.wp.y
        self.wp.x = wpy
        self.wp.y = -wpx
    def right(self, angle):
        turns = angle // 90
        for i in range(turns):
            self.right90()
    def left(self, angle):
        self.right( 360 - angle )
    def forward(self, times):
        for i in range(times):
            self.x += self.wp.x
            self.y += self.wp.y
    def distance(self):
        return abs(self.x) + abs(self.y)  # needs to be abs
    def __str__(self):
        return "({0.x!s},{0.y!s}) => {1!s}".format(self, self.distance())

s = Ship()
with open('2020/12/input.txt') as f:
    cmds = f.read()
    cmds = cmds.split("\n")
for cmd in [c for c in cmds if len(c) > 0]:
    
    c = cmd[0]
    a = int(cmd[1:])
    if c == "E":
        s.east(a)
    elif c == "S":
        s.south(a)
    elif c == "W":
        s.west(a)
    elif c == "N":
        s.north(a)
    elif c == "R":
        s.right(a)
    elif c == "L":
        s.left(a)
    elif c == "F":
        s.forward(a)
    else:
        raise "BOOM"

print( str(s) )