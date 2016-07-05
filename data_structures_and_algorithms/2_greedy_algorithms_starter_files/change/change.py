# Uses python3
import sys

def get_change(n):
	n=int((n/10.0)+0.5)+n%5
    #write your code here
	return n

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
