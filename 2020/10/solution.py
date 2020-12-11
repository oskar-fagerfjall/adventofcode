# Seems like it should be enough to sort an array and then step through it.

def count_adapters( s ):
    adapters = list( map(int, s.split()))
    adapters.append( max( adapters ) + 3 )
    adapters = sorted( adapters )
    jolt = 0
    counts = [0,0,0]
    for a in adapters:
        diff = a - jolt
        if diff > 3:
            raise "NoFittingAdapter"
        elif diff > 0:
            jolt += diff
            counts[diff-1] += 1
        else:
            pass
    return counts

