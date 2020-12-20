""" placeholder doctring """
from solution import arrival, allontime

with open("2020/13/input.txt") as f:
    indata = f.read()
indata = indata.split("\n")
t = int( indata[0] )
buses = indata[1].split(",")
buses = filter(lambda x: (x != "x"), buses)
buses = list( map( int, buses ))

print( t )
print( buses )
arrivesin = [arrival(b,t) for b in buses]
answer = min(arrivesin) * buses[arrivesin.index(min(arrivesin))]
print( min(arrivesin) )
print( buses[arrivesin.index(min(arrivesin))] )
print( answer )

#part 2

with open("2020/13/input.txt") as f:
    indata = f.read()
indata = indata.split("\n")
buses = indata[1].split(",")
buses = filter(lambda x: (x != "x"), buses)
buses = list( map( int, buses ))

interarrivals = indata[1].split(",")
arrivesafter = {}
i = 0
for c in interarrivals:
    if c != "x":
        arrivesafter[int(c)] = i
    i += 1
print(arrivesafter)

i = 0
i = 4822229849
while not allontime(arrivesafter, i):
    i += 19
print(i)
