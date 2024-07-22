'''
 Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

'''

# N is an odd number and M is 3 times N , create NxM mat design

input_line= input("Enter  value of N and M  : ")
N,M = map(int,input_line.split())

if M == 3*N:
    for i in range(1,int(N/2)+1):
        print(((2*i-1)*'.|.').center(M,'-'))
    print('WELCOME'.center(M,'-'))
    for i in range(int(N/2),0,-1):
        print(((2*i-1)*'.|.').center(M,'-'))


        # else:
        #     print((i*'.|.').center(M,'-'))
        #     print()
    