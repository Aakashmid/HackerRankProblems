# print largest prime factors

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    primeFactorsList=[]
    while n%2==0:
        primeFactorsList.append(2)            
        n//=2
    
    # use step value 2 because want to iterate only  odd number
    for i in range(3,int(n**0.5)+1,2):
        while n%i==0:
            primeFactorsList.append(i)            
            n//=i

    if n>2:
        primeFactorsList.append(n)
    print(max(primeFactorsList))