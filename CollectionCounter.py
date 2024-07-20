'''collections.Counter()
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
Sample Code
'''
# tasks find money earnd by shop keeper 

from collections import Counter


X =int(input())  # no. of shoes
ss_list=list(map(int,input().split()))   #shoes sizes list present in shop
N =int(input())  # no. of customer

shoes_dict=dict(Counter(ss_list))  # contains size as key and no. of shoes of that size

money_earned = 0

for i in range(N):
    shoe_size,amount=map(int,input().split())
    
    if shoe_size in shoes_dict.keys() and shoes_dict[shoe_size]>0:
        shoes_dict[shoe_size]-=1
        money_earned+=amount

print(money_earned)