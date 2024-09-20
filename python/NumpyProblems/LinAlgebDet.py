import numpy as np
N=int(input())
arr_list=[]
for _ in range(N):
    arr=list(map(float,input().split()))
    arr_list.append(arr)
result=np.linalg.det(arr_list)
print(round(result,2))