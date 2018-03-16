#!/bin/python3

import os
import sys
import collections


def countEquals(arrString, arrQueries):
    counter=collections.Counter(arrString)
    for x in arrQueries:
        print(counter[x])
        
    
if __name__ == '__main__':
    N = int(input())
    arrString = []
    arrQueries = []
    for x in range(N):
        arrString.append(input())

    Q = int(input())
    for z in range(Q):
        arrQueries.append(input())

    countEquals(arrString, arrQueries)
