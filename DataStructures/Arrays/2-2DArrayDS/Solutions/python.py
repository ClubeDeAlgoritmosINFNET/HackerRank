#!/bin/python3
#Author: Alexandre marcos

import sys

arr = []
hourGlass = []
def getHourglass(arr):
    highest = -1000
    for k in range(len(arr)-2):
        for x in range(len(arr)-2):
            top = arr[k][x:3+x]
            middle = arr[1+k][x+1:2+x]
            bottom = arr[2+k][x:3+x]
            totalGeral = sum(top+middle+bottom)
            
            if totalGeral > highest:
                highest = totalGeral
    
    print(highest)         

for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
getHourglass(arr)