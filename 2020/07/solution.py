class Bag:
    def __init__( self, color ):
        self.color = color
        self.contains = {}
        self.contained_by = {}
        
    def add( self, bag, quantity ):
        self.contains.add( bag, quantity )
        bag.contained_by.add( self )
        
bags = {}
for description in input: # first create all the nodes
    color = description.split(" bags contain ")[0]
    bags.add( color, Bag( color ))  # hashed lookup of string is faster
    
for description in input:  # then add the rules
    color, counts = description.split(" bags contain ")
    counts = counts.split().iter()
    try:
        while True:
            n = counts.next()
            c = " ".join( counts.next(), counts.next() )
            crap = counts.next()
            bags[color].add( bags[c], n )
    except StopIteration:
        pass

mybag = bags["shiny gold"]

def unpack( bag ):
    result = set()
    for b in bag.contained_by:
        result.union( unpack( b ) ) 
    return b
        
