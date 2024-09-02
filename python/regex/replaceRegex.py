# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
for _ in range(N):
    mystr=input()
    mystr=re.sub(r'\s&&\s',' and ',mystr)
    mystr=re.sub(r'\s\|\|\s',' or ',mystr)
    print(mystr)