#!/bin/python3

import sys

n = int(input())
arr = sorted(map(int, input().split()))

i = n - 3
while i >= 0 and (arr[i] + arr[i + 1] <= arr[i + 2]):
    i -= 1

if i >= 0:
    print(arr[i], arr[i + 1], arr[i + 2])
else:
    print(-1)
