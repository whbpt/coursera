# Uses python3
import sys
from math import *
def optimal_summands(n):
    summands = []
    guess=ceil(sqrt(n*2))
    for i in range(guess-2,guess+1):
        if i*i+i>2*n:
            num=i
            break
    for i in range(1,num):
        if n>=(2*i+1):
            summands.append(i)
        else:
            summands.append(n)
        n=n-i
    #write your code here
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
