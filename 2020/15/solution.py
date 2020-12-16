input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

class Rule:
    def __init__( self, s ):
        self.title, s = s.split(": ", 2)  # "row: 6-11 or 33-44"
        r1, r2 = s.split(" or ", 2)       # "6-11 or 33-44"
        low, high = r1.split("-")         # "6-11"
        self.f1 = int( low )              # 6
        self.t1 = int( high )             # 11
        low, high = r2.split("-")         # "33-44"
        self.f2 = int( low )              # 33
        self.t2 = int( high )             # 44
    def valid( self, i ):
        return (i >= self.f1 and i <= self.t1) or (i >= self.f2 and i <= self.t2)


# rules = [Rule("class: 1-3 or 5-7"),
#          Rule("row: 6-11 or 33-44"),
#          Rule("seat: 13-40 or 45-50")]

# tickets = """7,3,47
# 40,4,50
# 55,2,20
# 38,6,12
# """


with open("2020/15/input.txt", "r") as f:
    contents = f.read()

rules, mine, tickets = contents.split("\n\n", 3)
rules = rules.split("\n")
mine = mine.split("\n")[1]
tickets = tickets.split("\n")[1:]

rule = [Rule(s) for s in rules]

total = 0
for t in tickets:
    for i in t.split(","):
        valid = False
        for r in rule:
            if r.valid( int(i) ):
                valid = True
        if not valid:
            total += int(i)
print( total )
