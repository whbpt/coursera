# Uses python3
import numpy as np
def edit_distance(s, t):
	slen=len(s)
	tlen=len(t)
	array_=np.zeros([slen+1,tlen+1])
	for i in range(0,slen+1):
		array_[i,0]=i;
	for j in range(0,tlen+1):
		array_[0,j]=j;
	for i in range(1,slen+1):
		for j in range(1,tlen+1):
			if t[j-1]==s[i-1]:
				array_[i,j]=min(array_[i-1,j-1],array_[i,j-1]+1,array_[i-1,j]+1)
			else:
				array_[i,j]=min(array_[i-1,j-1]+1,array_[i,j-1]+1,array_[i-1,j]+1)
	return int(array_[slen,tlen])

if __name__ == "__main__":
	print(edit_distance(input(), input()))
