# Seems like it should be enough to sort an array and then step through it.
#
import itertools as it

def get_adapters( s ):
    adapters = set( map(int, s.split()))
    adapters.add( max( adapters ) + 3 )
    return sorted( list (adapters) )

def usable( jolt, adapter ):
    diff = adapter - jolt
    return diff >= 1 and diff <= 3

def count_adapters( s ):
    adapters = get_adapters( s )
    jolt = 0
    counts = [0,0,0]
    for a in adapters:
        if usable(jolt, a):
            diff = a - jolt
            jolt += diff
            counts[diff-1] += 1
    return counts

def _count2( joltage, adapters ):

    # if len( adapters ) == 0:
    #     return 0
    # elif usable(joltage, adapters[0]):
    #     return 1 + _count2(joltage + adapters[0], adapters[1:]) + _count2(joltage, adapters[1:])
    # else:
    #     return _count2(joltage, adapters[1:])
           
def count_adapters2( s ):
    adapters = get_adapters( s )

    return _count2( 0, adapters )

