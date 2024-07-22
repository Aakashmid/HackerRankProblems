'''The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.'''

from collections import defaultdict 

n,m=map(int,input().split())
ResultDict=defaultdict(list)

A=[]
B=[]

for i in range(n):
    A.append(input())
for i in range(m):
    B.append(input())


for i,val in enumerate(A):
    if val in B:
        ResultDict[val].append(i) 
    

for w in B:
    if len(ResultDict[w])==0:
        print(-1)
    else:
        for index in ResultDict[w]:
            print(index+1,end=' ')
        print()



