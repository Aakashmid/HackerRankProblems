
from  itertools import combinations_with_replacement

Mystr,r=input().split()  # here r is legth of combination and Mystr is string whose possible combinations we are findeing

Mystr=sorted(Mystr)
r=int(r)

allCombination=combinations_with_replacement(Mystr,r)
for c in allCombination:
    print(''.join(c))