# Uses python3
import sys
num=0
def merge(left,right):
    global num
    sorted=[] #array to store the sorted list
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            num=num+(len(left)-i)
            j+=1
    sorted+=left[i:]
    sorted+=right[j:]
    return sorted

def merge_sort(li):
    "function to compute merge-sort"
    if len(li)==1:
        return li
    middle=len(li)//2
    left_li=merge_sort(li[:middle])
    right_li=merge_sort(li[middle:])
    return merge(left_li,right_li)



def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    #print(get_number_of_inversions(a, b, 0, len(a)))
    merge_sort(a)
    print(num)
