import re

class Bag:
    def __init__( self, color ):
        self.color = color
        self.contains = {}
        self.contained_by = []
        
    def add( self, bag, quantity ):
        self.contains[bag] = quantity
        bag.contained_by.add( self )

with open( '2020/07/input.txt', 'r' ) as infile:
    rawrules = infile.read().split("\n")

bags = {}
colors, rules = [x.split(" bags contain ") for x in rawrules]
for color in colors: # first create all the nodes
    bags[color] = Bag( color )  # hashed lookup of string is faster
rules = [re.split(", |\.", r) for r in rules]
for rule in zip( colors, rules):
    color, ruleset = rule
    from_bag = bags[color]
    for r in ruleset:
        rc = r[1] + " " + r[2]
        to_bag = bags[ rc ]
        from_bag.add( to_bag, r[0] )


mybag = bags["shiny gold"]

def unpack( bag ):
    result = set()
    for b in bag.contained_by:
        result.union( unpack( b ) ) 
    return b
        
