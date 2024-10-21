#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())
    
    sorted_array = sorted(arr, key=lambda x: x[k])  # this functio sort  the arr based on kth value its element(list)
    for element in sorted_array:
        for i in element:
             print(i,end=' ')
        print()
