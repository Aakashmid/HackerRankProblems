'''
itertools.permutations(iterable[, r])=
This tool returns successive r length permutations of elements in an iterable.
If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.
Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

'''

from itertools import permutations

mystr,r= input().split()  # r is length of permutation element
r=int(r)
mystr=''.join(sorted(mystr))
permutations_listString=list(permutations(mystr,r))

for p_el in permutations_listString:
    permutaion_str=""
    for i in  range(r):
        permutaion_str=permutaion_str+p_el[i]
    print(permutaion_str)
