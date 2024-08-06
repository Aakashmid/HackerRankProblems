# task - find largest primefactor of a number

t = int(input().strip()) # number of test cases
for a0 in range(t):
    n = int(input().strip())  

    primeFactorsList=[]
    d=2
    while n >1:
        # adding all divisor to primeFactors (all divisors are prime factors )
        while n%d==0:
            primeFactorsList.append(d)
            n//=d
        d+=1
            
    print(max(primeFactorsList))


# note - all number can is divisible by any prime nuber