#!/bin/python3

import sys

def breakingRecords(scores):
    maxScore = scores[0]
    minScore = scores[0]
    breakMaxScore = 0
    breakMinScore = 0
    
    for score in scores:
        if score > maxScore:
            breakMaxScore += 1
            maxScore = scores[scores.index(score)]
        if score < minScore:
            breakMinScore += 1
            minScore = scores[scores.index(score)]
        
    return(breakMaxScore, breakMinScore)
    
    

if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    result = breakingRecords(scores)
    print (" ".join(map(str, result)))


