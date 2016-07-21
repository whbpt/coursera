#Uses python3

import sys
import numpy as np
def edit_distance(ss, tt, kk):
    global big_
    slen=len(ss)
    tlen=len(tt)
    klen=len(kk)
    array_=np.zeros([slen+1,tlen+1,klen+1])
    for i in range(1,slen+1):
        for j in range(1,tlen+1):
            for k in range(1,klen+1):
                if ss[i-1]==tt[j-1] and tt[j-1]==kk[k-1]:
                    array_[i,j,k]=array_[i-1,j-1,k-1]+1
                else:
                    array_[i,j,k]=max(array_[i-1,j,k],array_[i,j-1,k],array_[i,j,k-1])
    return int(array_[slen,tlen,klen])
def lcs3(a, b, c):
    #write your code here
    temp_=edit_distance(a,b,c)
    return temp_
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
