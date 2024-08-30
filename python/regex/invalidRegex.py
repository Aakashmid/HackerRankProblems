# find out where given string is valid regex or not
import re
T=int(input())
    
for i in range(T):
    s=input()
    if any(op + '+' in s for op in ['*', '+', '?']):
        print("False")
    else:
        try:
            re.compile(s)
            print('True')
        except re.error:
            print('False')
        