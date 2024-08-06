#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fibonacciSr=[1,2]
    
    secondLastEl=fibonacciSr[len(fibonacciSr)-2]
    lastEl=fibonacciSr[len(fibonacciSr)-1]
    while  (lastEl+secondLastEl) < n:
        fibonacciSr.append(lastEl+secondLastEl)
        secondLastEl=lastEl
        lastEl=fibonacciSr[len(fibonacciSr)-1]
    
    print(sum(num for num in fibonacciSr  if num%2==0))