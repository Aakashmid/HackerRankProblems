'''numpy.min and numpy.max method return minimum and maximum value from an array along a given axis respectively. If axis is not specified, the methods return minimum and maximum value from the flattened array.
eg .my array is  [[1,2],[3,4],[4,7]] ,  min along axis 1 is [1,3,4] and max along axis 1 is [2,4,7] , min along axis 0  is [1,2] and max along axis 0 is [4,7]
'''
import numpy as np
N,M=tuple(map(int,input().split()))
myList=[]
for i in range(N):
    myList.append(list(map(int,input().split())))

myArray=np.array(myList)
min_along_1=np.min(myList,axis=1)
print(np.max(min_along_1))   # print max of min of 1st axis

# -----------------------------
# mean , std ,variance in numpy 
import numpy as np
N,M=tuple(map(int,input().split()))
Mylist=[] 
for _ in range(N):
    Mylist.append(list(map(int,input().split())))

myArray=np.array(Mylist)  # it is numpy array 
print(np.mean(myArray,axis=1)) # mean along axis 1
print(np.var(myArray,axis=0)) # variance along axis 0
print(round(np.std(myArray,axis=None),11)) # standard deviation along flattened array
