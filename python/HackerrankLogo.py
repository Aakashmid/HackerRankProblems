# print this logo for every odd(number)

'''
    H
   HHH
  HHHHH
 HHHHHHH
HHHHHHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
                    HHHHHHHHH
                     HHHHHHH
                      HHHHH
                       HHH
                        H
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
width=int(input())
ch='H'

for i in range(width):
    print((ch*i).rjust(width-1)+ch+(ch*i).ljust(width-1))

for i in range(width+1):
    print((int(width/2))*" " +(ch*width).ljust(width*4)+(ch*width).ljust(width*4))

for i in range(int(width/2)+1):
    print((int(width/2))*" "+ ch*5*width)

for i in range(width+1):
    print((int(width/2))*" "+(ch*width).ljust(width*4)+(ch*width).ljust(width*4))

for i in range(width):
    print((int(width/2))*"  "+((ch*(width-i-1)).rjust(width-1)+ch+(ch*(width-1-i)).ljust(width-1)).rjust(width*5))


# >>> width = 20
# >>> print 'HackerRank'.ljust(width,'-')
# HackerRank----------  