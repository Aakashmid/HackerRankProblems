testCasesNo=int(input())

for _ in range(testCasesNo):
    try:
        val1 , val2 = input().split()
        print(int(val1)//int(val2))
    except Exception as e:
        print(f'Error Code: {e}')