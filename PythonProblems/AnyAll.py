'''print true if all number is positive and any number in that is pallindrom else print false'''

N=int(input())
data_list=list(map(int,input().split()))
print(any([str(num) == str(num)[::-1] for num in data_list])) if all([i>=0 for i in data_list]) else print(False)

    