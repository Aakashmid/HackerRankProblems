'''
You are given a list of N lowercase English letters. For a given K integer , you can select any K indices (assume  1 -based indexing) with a uniform probability from the list.
'''

from itertools import combinations
N=int(input())
my_list=input().split()
k=int(input())
p_t=list(combinations(my_list,k))
lagc=0
for t in p_t: # iterating tuple
    if any(t[i]=='a' for i in range(len(t))):  # checking whether any letter is 'a' in tuple 
        lagc+=1     
print(float(lagc)/float(len(p_t)))