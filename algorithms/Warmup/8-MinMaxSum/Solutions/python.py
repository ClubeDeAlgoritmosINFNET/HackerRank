import sys

def miniMaxSum(arr):
    max=-sys.maxsize #Python int 64-bit
    min=sys.maxsize  #Python int 64-bit
    sum=0
    for x in arr:
        sum+=x
        if x>max:
            max=x
        if x<min:
            min=x
    print (sum-max,sum-min)

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)