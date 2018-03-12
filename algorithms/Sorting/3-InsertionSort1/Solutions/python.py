#!/bin/python3
import sys

def insertion_sort(n, arr):
    e = arr[-1]

    for i in range(n - 2, -2, -1):
        if arr[i] <= e or i == -1:
            arr[i + 1] = e
            print(' '.join(arr))
            break

        arr[i + 1] = arr[i]

        print(' '.join(arr))


n = int(input().strip())
arr = input().strip().split(' ')
insertion_sort(n, arr)
