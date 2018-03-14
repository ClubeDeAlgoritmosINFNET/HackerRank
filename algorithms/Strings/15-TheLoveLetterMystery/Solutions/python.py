#!/bin/python3
import sys

def theLoveLetterMystery(s):
    out = 0

    for i in range(len(s) // 2):
        out += abs(ord(s[i]) - ord(s[len(s) - i - 1]))
    return out

q = int(input().strip())

for _ in range(q):
    s = input().strip()
    result = theLoveLetterMystery(s)
    print(result)
