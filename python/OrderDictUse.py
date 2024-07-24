'''
collections.OrderedDict
An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.
'''
from collections import OrderedDict
N=int(input())

ItemsDict=OrderedDict()

for i in range(N):
    inputs=input().split()
    itemName=''
    price=int(inputs[len(inputs)-1])
    for el in range(len(inputs)-1):
        itemName+=inputs[el]+" "
        
    if itemName in  ItemsDict:
        ItemsDict[itemName]+=int(price)
    else:
        ItemsDict[itemName]=int(price)

for item in ItemsDict:
    print(f'{item}{ItemsDict[item]}')
