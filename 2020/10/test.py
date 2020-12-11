from solution import count_adapters

a = """16
10
15
5
1
11
7
19
6
12
4
"""

result = count_adapters( a )
expected = [7, 0, 5]

print( str(result) + " == " + str(expected))

b = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

result = count_adapters( b )
expected = [22, 0, 10]

print( str(result) + " == " + str(expected))

with open("2020/10/input.txt", "r") as infile:
    result = count_adapters( infile.read() )
    print( str(result) )
    print( str( result[0] * result [2] ))