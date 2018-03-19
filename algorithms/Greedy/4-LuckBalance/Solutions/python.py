#!/bin/python3

import sys

# Solution
def luckBalance(n, k, contests):
    luck = 0
    important_contests = []

    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]
        else:
            important_contests.append(contest[0])

    important_contests.sort(reverse=True)

    luck -= sum(important_contests[k:])
    luck += sum(important_contests[:k])

    return luck

# Input boilerplate
if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    contests = []
    for contests_i in range(n):
       contests_t = [int(contests_temp)
                     for contests_temp in input().strip().split(' ')]
       contests.append(contests_t)
    result = luckBalance(n, k, contests)
    print(result)
