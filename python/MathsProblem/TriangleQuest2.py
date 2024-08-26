'''
print  pattren in one line
1  
121
12321
1234321
123454321
'''
for i in range(1,int(input())+1):
    print(sum(map(lambda d:10**d,range(i)))**2)  # 1*1, 11*11 , 111*111 etc 