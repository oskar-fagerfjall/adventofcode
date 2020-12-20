def binarize( s = ''):
    return s.replace("L", "0").replace("R", "1").replace("F", "0").replace("B","1")

def decimalize( b ):
    return int( b.zfill(8), 2)

class Seat(object):
    def __init__( self, line ):
        self.line = line
        self.row = decimalize( binarize( self.line[0:7] ))
        self.col = decimalize( binarize( self.line[7:]  ))
        self.id  = self.row * 8 + self.col 

maxid = 0
ids = []
with open('2020/05/input.txt', 'r') as infile:
    while True:
        line = infile.readline().strip()
        if not line or not len(line) == 10:
            break
        s = Seat( line )
        ids.append(s.id)
        if s.id > maxid:
            maxid = s.id
print( maxid ) # part 1
ids = sorted( ids )

currentseat = ids[0]
for i in ids[1:]:
    if not i == currentseat + 1:
        print(currentseat + 1) # part 2
    currentseat = i
    