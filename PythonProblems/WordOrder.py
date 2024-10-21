'''task is to print number of occurence of a word in order of they input '''

from collections import defaultdict

n=int(input())
mywords=defaultdict(int)  

for _ in range(n):
    words=input()
    mywords[words]+=1
    


print(len(mywords))
for word in mywords:
    print(mywords[word],end=' ')