cube = lambda x: x**3 

def fibonacci(n):
    fib_numbers=[]
    for i in range(n):
        if (i<=1):
            fib_numbers.append(i)
        else:
            fib_numbers.append(fib_numbers[i-1]+fib_numbers[i-2])    
    
    return fib_numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))