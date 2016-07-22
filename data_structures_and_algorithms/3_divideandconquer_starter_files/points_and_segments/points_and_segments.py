# Uses python3
import sys
import numpy as np
def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    points_=[]
    for i in range(0,len(points)):
        points_.append([points[i],i])
    points_.sort()
    starts.sort()
    ends.sort()
    i,j=0,0
    count_=[0]*len(points)
    starts.append(points_[-1][0]+1)
    ends.insert(0,points_[0][0]-1)
    while i<len(starts) and j<len(points_):
        if points_[j][0]<starts[i]:
            count_[j]=i
            j+=1
        else:
           i+=1
    i=len(ends)-1
    j=len(points_)-1
    mark_=[len(ends)]*len(points)
    while i>=0 and j>=0:
        if points_[j][0]>ends[i]:
            mark_[j]=i
            j-=1
        else:
            i-=1
    for i in range(0,len(points)):
        cnt[points_[i][1]]=count_[i]-mark_[i] 
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
#    cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
    print()
