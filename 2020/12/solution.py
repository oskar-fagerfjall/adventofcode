distance = 25

class Ship:
    def __init__( self ):
        self.x = 0
        self.y = 0
        self.direction = 0
    def north(self, dist):
        self.y += dist
    def south(self, dist):
        self.y -= dist
    def east(self, dist):
        self.x += dist
    def west( self, dist):
        self.x -= dist
    
    dirs = {0: east, 90: south, 180: west, 270: north}
    def right(self, angle):
        self.direction = (self.direction + angle) % 360
    def left(self, angle):
        self.direction = (self.direction - angle) % 360
    def forward(self, dist):
        self.dirs[self.direction](self, dist)
    def distance(self):
        return abs(self.x) + abs(self.y)  # needs to be abs
    def __str__(self):
        return "({0.x!s},{0.y!s}) => {1!s}".format(self, self.distance())

s = Ship()
s.forward(10)
s.north(3)
s.forward(7)
s.right(90)
s.forward(11)
print( str(s) )

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