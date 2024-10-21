import numpy as np

A=np.array(list(map(int,input().split())))
B=np.array(list(map(int,input().split())))

print(np.inner(A,B))  # inner method return inner product of two array (eg. for A,B - it returns a1b1+a2b2+...)
print(np.outer(A,B)) # returns outer product ( returns an array consisting of arrays , [[a1b1,a1b2,..], [a2b1,a2b2,...]])
