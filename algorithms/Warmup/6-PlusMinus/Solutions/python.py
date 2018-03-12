#!/bin/python3

import sys
from decimal import *

def plusMinus(arr):
    getcontext().prec = 6
    positive = 0
    negative = 0
    zero = 0

    for x in arr:
        if x > 0:
            positive = positive + 1
        if x < 0:
            negative = negative + 1
        if x == 0:
            zero = zero + 1
    
    print(Decimal(positive)/Decimal(n))
    print(Decimal(negative)/Decimal(n))
    print(Decimal(zero)/Decimal(n))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
