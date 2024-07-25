from itertools import groupby

groups=[]
mystr = input()
for key, group in groupby(mystr):
    groups.append(list(group))

for gr in groups:
    print((len(gr),gr[0]),end=' ')