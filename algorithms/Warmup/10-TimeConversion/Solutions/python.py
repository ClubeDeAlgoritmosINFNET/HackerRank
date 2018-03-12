#!/bin/python3

import sys
from datetime import datetime

def timeConversion(s):
    in_time = datetime.strptime(s, "%I:%M:%S%p")
    out_time = datetime.strftime(in_time, "%H:%M:%S")
    return out_time
 

s = input().strip()
result = timeConversion(s)
print(result)
a