# Uses python3
import sys
from math import *
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    if left + 2 == right:
        if a[1]==a[0]:
            return 0
        else:
            return -1
    a.sort()
    right=right-1
    tag_=a[ceil(right/2)]
    left1,right1=left,floor(right/2)
    left2,right2=ceil(right/2),right
    len1_=ceil(right/2)
    len2_=ceil(right/2)
    if a[left1]==tag_:
        len1_=left1
    else:
        for i in range(round(len(a)/2)):
            middle1=floor((left1+right1)/2)
            if a[middle1]==tag_:
                right1=middle1
            else:
                left1=middle1
            if right1-left1<=1:
                if a[right1]==tag_ and a[left1]!=tag_:
                    len1_=right1
                    break
    if a[right2]==tag_:
        len2_=right2
    else:
        for i in range(round(len(a)/2)):
            middle2=floor((left2+right2)/2)
            if a[middle2]==tag_:
                left2=middle2
            else:
                right2=middle2
            if right2-left2<=1:
                if a[left2]==tag_ and a[right2]!=tag_:
                    len2_=left2
                    break 
    if (len2_-len1_+1)>int(n/2):
        return 0
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
