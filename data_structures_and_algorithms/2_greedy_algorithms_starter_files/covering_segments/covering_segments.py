# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    aaa=[]
    for (a,b) in segments:
        aaa.append([a,b])
    aaa.sort()
    lastlist_=aaa[0]
    for list_ in aaa:
        if lastlist_[1]>=list_[0]:
            lastlist_=[max(lastlist_[0],list_[0]),min(lastlist_[1],list_[1])]
        else:
            points.append(lastlist_[1])
            lastlist_=list_
    points.append(lastlist_[1])
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
