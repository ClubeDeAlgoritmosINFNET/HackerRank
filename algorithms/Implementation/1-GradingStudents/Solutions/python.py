#!/bin/python3

import sys

def solve(grades):
    finalGrade = []
    for grade in grades:
        newGrade = GetNextMultiple(grade)
        
        if (newGrade - grade) < 3 and grade >= 38:
            grade = newGrade
            finalGrade.append(grade)
            
        elif (newGrade - grade) >= 3 or grade < 38:
            finalGrade.append(grade)
            
    return finalGrade
         
def GetNextMultiple(grade):
    while grade%5 != 0:
        grade += 1
        
    newGrade = grade
    return newGrade

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
