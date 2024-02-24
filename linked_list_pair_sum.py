def linkedlistpairsum(ll,head):
    fast=slow=head
    next=None
    previous=None
    while fast and fast.next:
        fast=fast.next.next
        temp=slow.next
        slow.next=previous
        previous=slow
        slow=temp
    maximum=0
    while slow:
        maximum=max(maximum,slow.val+previous.val)
        previous=previous.next
        slow=slow.next
    return maximum


#finding the kth largest element of an arrray
#method1
def find_largest(arry,k):
    for i in range(k-1):
        arry.remove(max(arry))
    return max(arry)
a=[8,9,1,2,3,]
print(find_largest(a,3))
#method2
def find_large(arr,k1):
    n=len(arr)
    arr.sort()
    return arr[n-k1]


