'''
Read in two integers,  and , and print three lines.
The first line is the integer division  (While using Python2 remember to import division from __future__).
The second line is the result of the modulo operator: .
The third line prints the divmod of  and .
'''
a=int(input())
b=int(input())

print(a//b)
print(a%b)
print(divmod(a,b))