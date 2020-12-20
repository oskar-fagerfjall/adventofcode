""" placeholder doctring """
import solution

with open( "2020/20/testinput.txt" ) as f:
    indata = f.read()
    indata = indata.split("\n\n")
    for line in indata:
        line = line.split("\n")
        tid = line[0].split()[1]
        tid = tid.split(":")[0]
        tid = int( tid )
        t = solution.Tile()
        t.number = tid
        for row in [ x for x in line[1:] if len(x) > 0 ]:
            t.arr.append(row)
