'''
Task - Perform append, pop, popleft and appendleft methods on an empty deque .

- input method name and its value and apply it on deque
'''

from collections import deque

N=int(input())
d=deque()
for _ in range(N):
    Input=input()
    if 'a' in Input.lower():
        value=int(Input.split()[1])
        d.appendleft(value) if 'l' in Input.lower() else d.append(value)

    elif 'p' in Input.lower():
        d.popleft() if 'l' in Input.lower() else d.pop()

for i in d:
    print(i,end=' ')
            
        
