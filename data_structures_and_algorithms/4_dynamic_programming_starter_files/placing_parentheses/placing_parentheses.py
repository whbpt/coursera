# Uses python3
import numpy as np
def evalt(a, b, op):
	if op == '+':
		return a + b
	elif op == '-':
		return a - b
	elif op == '*':
		return a * b
	else:
		assert False

def get_maximum_value(dataset):
	#write your code here
	count=0
	list_=[]
	op_=[]
	for line in dataset.split()[0].split("*"):
		for line2 in line.split("-"):
			for line3 in line2.split("+"):
				list_.append(line3)
	for line in dataset:
		if line in ["*","-","+"]:
			op_.append(line[0].strip())
#	print(list_[0],end="")
#	for i in range(1,n):
#		print(op_[i-1],end="")
#		print(list_[i],end="")
#	print()
	n=len(list_)
	array_m=np.zeros([n,n])
	array_M=np.zeros([n,n])
	for i in range(0,n):
		array_m[i,i]=list_[i]
		array_M[i,i]=list_[i]
	for s in range(1,n):
		for i in range(0,n-s):
			j=i+s
			min_=99999999
			max_=-99999999
			for k in range(i,j):
				a=evalt(array_M[i,k],array_M[k+1,j],op_[k])
				b=evalt(array_M[i,k],array_m[k+1,j],op_[k])
				c=evalt(array_m[i,k],array_M[k+1,j],op_[k])
				d=evalt(array_m[i,k],array_m[k+1,j],op_[k])
				min_=min(min_,a,b,c,d)
				max_=max(max_,a,b,c,d)
				array_m[i,j]=min_
				array_M[i,j]=max_
	return int(array_M[0,n-1])


if __name__ == "__main__":
	print(get_maximum_value(input()))
