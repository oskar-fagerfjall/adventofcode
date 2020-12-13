with open('2020/06/input.txt', 'r') as infile:
    input = infile.read()

total, total2 = 0, 0

groups = input.split("\n\n")
for group in groups:
    unique_answers = set()
    group_answers = []
    for participant in group.split():
        my_answers = []
        for answer in participant:
            my_answers.append(answer)
            unique_answers.add(answer)   
        group_answers.append(my_answers)
    total += len(unique_answers)
    if len(group_answers) > 0:
        s = set( group_answers[0] )
        for ans in group_answers[1:]:
            s = s.intersection(ans)
        total2 += len( s ) 
print( "solution part 1 = " + str(total) )
print( "solution part 2 = " + str(total2) )