import re
N = int(input())
for i in range(N):
    num_str=input()
    match=re.search(r'\b[7-9]\d{9}\b',num_str)
    if match :
        print("YES")
    else:
        print('NO')