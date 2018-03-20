
#!/bin/python3
import sys

def printArray(arr):
    for element in reversed(arr):
        print(element, end=" ")
            
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    printArray(arr)