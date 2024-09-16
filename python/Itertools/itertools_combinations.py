'''
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]

'''


from itertools import combinations

StringS,SizeK=input().split()

StringS=sorted(StringS)
SizeK=int(SizeK)

for i in range(1,SizeK+1):
    Combinations=list(combinations(StringS,i))
    for c in Combinations:
        print(''.join(c))