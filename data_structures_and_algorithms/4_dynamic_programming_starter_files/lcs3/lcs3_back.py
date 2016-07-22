#Uses python3

import sys
import numpy as np
big_=[]
def getMinIndex(my_list):
    index_=list()
    for i in range(0,len(my_list)):
        if min(my_list)==my_list[i]:
            index_.append(i)
    return index_
def recal(result_,array2,ii,jj,kk):
    result2=result_.copy()
    result2.append([ii,jj,kk])
    if ii!=0 and jj!=0 and kk!=0:
        a=[array2[ii,jj,kk],ii,jj,kk]
        b=[array2[ii-1,jj,kk],ii-1,jj,kk]
        c=[array2[ii,jj-1,kk],ii,jj-1,kk]
        d=[array2[ii,jj,kk-1],ii,jj,kk-1]
        e=[array2[ii-1,jj-1,kk-1],ii-1,jj-1,kk-1]
        if e[0]+1==a[0]:
            print(result_)
            recal(result2,array2,e[1],e[2],e[3])
        else:
            temp2_=[b[0],c[0],d[0],e[0]]
            temp_=[b,c,d,e]
            index_=getMinIndex(temp2_)
            for i in range(0,len(index_)):
                recal(result2,array2,temp_[index_[i]][1],temp_[index_[i]][2],temp_[index_[i]][3])
def edit_distance(ss, tt, kk):
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
    recal([],array_,slen,tlen,klen)
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
