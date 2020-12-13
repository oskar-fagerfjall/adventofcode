import itertools as it
import functools as ft 
import operator as op

def possible_sums( nums ):
    combs = it.combinations( nums, 2 )   # list of tuples
    return [ ft.reduce( op.add, c ) for c in combs ]  # combine those tuples

def sums_to( sum, nums ):
    for i in range( len( nums )):
        currentlist = nums[0:i+1]
        if ft.reduce( op.add, currentlist ) == sum:
            smallest = min(currentlist)
            largest = max(currentlist)
            return  smallest + largest
    return sums_to( sum, nums[1:] )

def solution1( x ):    
    i1 = 0
    i2 = 25
    for n in x[i2:]:
        if not n in possible_sums( x[i1:i2] ):
            return n
        else:
            i1 += 1
            i2 += 1

with open('2020/09/input.txt', 'r') as infile:
    mylist = list( map( int, infile.read().split()))

print( solution1( mylist ) )
print( sums_to( solution1( mylist ), mylist ))


    # part 1: 20874512
    # part 2: 3012420