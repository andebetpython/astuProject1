def longest_sub_array(arr):
    maximum=0
    pointer=0
    i=0
    while i<len(arr):
        if arr[i]<arr[i-1]:
            pointer=i
        maximum=max(maximum,i-pointer+1)
        i+=1
    return maximum
a=[1,2,3,2,7]
print(longest_sub_array(a))
def two_sum(ar,target):
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if ar[i]+ar[j]==target:
                return (ar[i],ar[j])
g=[5,1,3,9,2]
print(two_sum(g,8))
#nlogn
def method_two(arrrr,tar):
    left=0
    right=len(arrrr)-1
    arrrr.sort()
    while left<=right:
        if arrrr[left]+arrrr[right]==tar:
            return arrrr[left],arrrr[right]
        elif arrrr[left]+arrrr[right]<tar:
            left+=1
        else:
            right-=1
print(method_two(g,8))
#findingthe first and last indece of reapeted element of sorted arrray
def reap(lis1,t):
    left=0
    right=len(lis1)-1
    start=0
    last=0
    while left<=right:
        if lis1[left]==t:
            start=left
        elif lis1[right]==t:
            last=right
        else:
            left+=1
            right-=1
    return start,last
p=[1,2,3,4,4,4,4,5,6]
print(reap(p,4))





