# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            continue
    a[l], a[j] = a[j], a[l]
    return j

    pass

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            print(a,a[i],a[j],x,"13-")
            a[i], a[j] = a[j], a[i]
            print(a,a[i],a[j],x,"13")
    a[l], a[j] = a[j], a[l]
    print(a,a[l],a[j],x,"14")
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);
def tricksort(a):
    dict_=dict()
    list_=list()
    for i in a:
        if i not in dict_.keys():
            dict_[i]=1
        else:
            dict_[i]=dict_[i]+1
    for key in dict_:
        #for i in range(0,dict_[key]):
        list_.append([key,dict_[key]])
    list_.sort()
    list2_=list()
    for i in list_:
        for j in range(0,i[1]):
            list2_.append(i[0])
    return list2_
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #randomized_quick_sort(a, 0, n - 1)
    for x in tricksort(a):
        print(x, end=' ')
    print()
