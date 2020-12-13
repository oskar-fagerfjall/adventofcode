import re

class Bag:
    def __init__( self, color ):
        self.color = color
        self.contains = {}
        self.contained_by = []
        
    def add( self, bag, quantity ):
        self.contains[bag] = quantity
        bag.contained_by.append( self )

    def find_bag( self, bag ):
        if self.color == bag.color:
            return True
        for b in self.contains:
            p = b.find_bag( bag )
            if p:
                return True
        return False     

    def num_bags_within( self ):
        total = 0
        for b in self.contains:
            q = self.contains[b]
            total += int( q )
            total += b.num_bags_within()
        return total

    def __str__( self ):
        return self.color + " bag"

with open( '2020/07/input.txt', 'r' ) as infile:
    rawrules = infile.read().split("\n")

# infile = """light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags."""





#rawrules = infile.split("\n")

bags = {}
for rawrule in rawrules:
    if len(rawrule) > 0:
        color, rules = rawrule.split(" bags contain ", 2)
        bags[color] = Bag( color )

for rawrule in rawrules:
    if len(rawrule) == 0:
        continue 
    color, rules = rawrule.split(" bags contain ", 2)
    rules = re.split(", |\.", rules)
    for r in rules:
        if len(r) > 0:
            r = r.split()
            if r[0] != "no":
                c = r[1]  + " " + r[2]
                q = r[0]
                bags[color].add( bags[c], q )

# def unpack( bag, bags ):
#     result = set()
#     for c, q in bag.items():
#         result.add( c )
#         result.union( unpack( bags[c], bags )) 
#     return result

found = []
for c, b in bags.items():
    if b.find_bag( bags["shiny gold"] ) and b != bags["shiny gold"]:
        found.append( b )

print( str( len( found )))

print( str( bags["shiny gold"].num_bags_within() ))
# for color,contents in bags.items():
#     can_contain =  unpack( contents, bags )
#     if "shiny gold" in can_contain:
#         print( str( color ))
