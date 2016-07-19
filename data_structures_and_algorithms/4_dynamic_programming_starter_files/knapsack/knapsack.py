# Uses python3
import sys
import numpy as np
def optimal_weight(W, w):
	# write your code here
	result = 0
	n= len(w)
	array_=np.zeros([n+1,W+1])
	for j in range(0,n):
		for i in range(1,W+1):
			if i-w[j]>=0:
				if array_[j,i-w[j]]+w[j]<=W:
					array_[j+1,i]=max(array_[j,i-w[j]]+w[j],array_[j,i])
			else:
				array_[j+1,i]=array_[j,i]
	return int(array_[n,W])

if __name__ == '__main__':
	input = sys.stdin.read()
	W, n, *w = list(map(int, input.split()))
	print(optimal_weight(W, w))
