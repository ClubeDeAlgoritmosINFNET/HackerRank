#!/bin/python3

import sys

def staircase(n):
    blank = ' '
    blankCount = n
    hashChar = '#'
    hashesCount = 0

    for x in range(n):
        blankCount = blankCount - 1
        hashesCount += 1
        print(blankCount*blank + hashesCount*hashChar)


if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)