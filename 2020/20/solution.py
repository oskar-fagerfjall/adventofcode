""" placeholder doctring """

class Tile:
    """ an image title that can be flipped and rotated """
    def __init__(self):
        self.arr = []  # 2D array
        self.identifier  = 0

    def load(self, raw_input):
        """ parse a tile representation """
        lines = raw_input.split("\n")
        tid = lines[0].split()[1]
        tid = tid.split(":")[0]
        self.identifier = int( tid )
        for row in lines[1:]:
            if row:
                row = row.replace(".", "0").replace("#", "1")
                self.arr.append(row)

    def flip_vt( self ):
        self.arr = self.arr.reverse()

    def flip_hz( self ):
        self.arr = [ r.reverse() for r in self.arr ] 

    def rotate( self ):
        self.arr = [ self.get_col(i) for i in range(10) ]

    def get_col(self, index):
        return [ r[index] for r in self.arr ]

    def top(self):
        return self.arr[0]

    def bottom(self):
        return self.arr[9]

    def right(self):
        return self.get_col(9)

    def left(self):
        return self.get_col(0)
