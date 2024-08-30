'''Find where A is strict superset or not'''
# A strict superset has at least one element that does not exist in its subset.
A=set(list(map(int,input().split())))
N=int(input())
Result=False
for i in range(N) :
    temp_set=set(list(map(int,input().split())))
    if temp_set.issubset(A) and len(A-temp_set) > 0:
        Result=True
    else:
        Result=False
        break
print(Result)