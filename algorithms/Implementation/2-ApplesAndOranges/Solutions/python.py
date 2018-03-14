#!/bin/python3

import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleInHouse = 0
    orangesInHouse = 0
    distanceHouseAppleTree = s - a
    distanceHouseOrangeTree = b - t
    houseSize = t-s
    
    for appleFall in apples:
        if appleFall >= distanceHouseAppleTree and appleFall <= distanceHouseAppleTree + houseSize:
            appleInHouse += 1
        
    for orangeFall in oranges:
        if orangeFall < 0:
            if abs(orangeFall) >= distanceHouseOrangeTree and abs(orangeFall) <= distanceHouseOrangeTree + houseSize:
                orangesInHouse += 1
                
    print(appleInHouse)
    print(orangesInHouse)

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    countApplesAndOranges(s, t, a, b, apple, orange)
