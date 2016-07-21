#Uses python3

import sys
import numpy as np
big_=[]
def getMinIndex(my_list):
    index_=list()
    for i in range(0,len(my_list)):
        if max(my_list)==my_list[i]:
            index_.append(i)
    return index_
def recal(result_,array2,ii,jj):
    global big_
    result2=result_.copy()
    result2.append([ii,jj])
    if ii!=0 and jj!=0:
        a=[array2[ii,jj],ii,jj]
        b=[array2[ii-1,jj],ii-1,jj]
        c=[array2[ii,jj-1],ii,jj-1]
        d=[array2[ii-1,jj-1],ii-1,jj-1]
        temp2_=[b[0],c[0],d[0]]
        temp_=[b,c,d]
        recal(result2,array2,temp_[getMinIndex(temp2_)[0]][1],temp_[getMinIndex(temp2_)[0]][2])
        if len(getMinIndex(temp2_))>=2:
            recal(result2,array2,temp_[getMinIndex(temp2_)[1]][1],temp_[getMinIndex(temp2_)[1]][2])
        if len(getMinIndex(temp2_))==3:
            recal(result2,array2,temp_[getMinIndex(temp2_)[2]][1],temp_[getMinIndex(temp2_)[2]][2])
#    elif ii==0 and jj!=0:
 #       recal(result2,array2,ii,jj-1)
  #  elif ii!=0 and jj==0:
   #     recal(result2,array2,ii-1,jj)
    else:
    #    result_.append([0,0])
        big_.append(result_) 


def edit_distance(ss, tt):
    global big_
    mmm=-1
    slen=len(ss)
    tlen=len(tt)
    array_=np.zeros([slen+1,tlen+1])
    for i in range(0,slen+1):
        array_[i,0]=0;
    for j in range(0,tlen+1):
        array_[0,j]=0;
    for i in range(1,slen+1):
        for j in range(1,tlen+1):
            if tt[j-1]==ss[i-1]:
                array_[i,j]=max(0,array_[i-1,j-1]+1)
            else:
                array_[i,j]=max(0,array_[i,j-1],array_[i-1,j])
    result=[]
    print(array_)
    recal(result,array_,slen,tlen)
    transall_=[]
    for lines in big_:
        tran_=[]
        for i in range(0,len(lines)-1):
            if array_[lines[i][0],lines[i][1]]==array_[lines[i+1][0],lines[i+1][1]]:
                if lines[i][0]!=0 and lines[i][1]!=0:
                    if ss[lines[i][0]-1]==tt[lines[i][1]-1]:
                        tran_.append(ss[lines[i][0]-1])
                     #   print(tran_)
        tran_.reverse()
        if tran_ not in transall_ and len(tran_)>0:
            transall_.append(tran_)
    return transall_
def rot(a,b,c):
    global big_
    temp_=edit_distance(b,a)
    temp2=[]
#    for line in temp_:
 #       big_=[]
#        for ii in edit_distance(c,line):
 #           temp2.append(ii)
    max1=0
   # for i in temp2:
    #    if len(i)>max1:
     #       max1=len(i)
    return max1
def lcs3(a, b, c):
    #write your code here
    max1=rot(a,b,c)
    #max2=rot(c,b,a)
    #max3=rot(a,c,b)
    return max1#(max1,max2,max3)

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
