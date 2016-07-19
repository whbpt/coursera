# Uses python3
import sys

def optimal_sequence(n):
	sequence = []
	dict_=dict()
	dict_[1]=[1]
	dict_[2]=[1,2]
	dict_[3]=[1,3]
	for i in range(4,n+1):
		if i%3==0 :
			sequence3=len(dict_[int(i/3)])
		else :
			sequence3=n
		if i%2==0 :
			sequence2=len(dict_[int(i/2)])
		else:
			sequence2=n
		sequence1=len(dict_[i-1])
		if sequence3<sequence2:
			if sequence3<sequence1:
				dict_[i]=dict_[int(i/3)].copy()
		if sequence2<=sequence3:
			if sequence2<sequence1:
				dict_[i]=dict_[int(i/2)].copy()
		if sequence1<=sequence3:
			if sequence1<=sequence2:
				dict_[i]=dict_[i-1].copy()
		dict_[i].append(i)
	return dict_[n]	
input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
