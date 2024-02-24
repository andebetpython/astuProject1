def rec(list):
    for i in range(0,len(list)-1):
        list[i],list[i+1]=list[i+1],list[i]
    return list




def selcetion_sort(array):
    for i in range(len(array)-1):
        minimum=array[i]
        for j in range(i+1,len(array)):
            if array[j]<minimum:
                minimum=array[j]
        minimum_endex=array.index(minimum,i)
        if array[i]!=array[minimum_endex]:
            array[i],array[minimum_endex]=array[minimum_endex],array[i]
    return array
arr=[8,5,1,3,5,9,21,4]
print(selcetion_sort(arr))
def bubble_sort(ar):
    for i in range(len(ar)):
        for j in range(len(ar)):
            if j>0 and ar[j]<ar[j-1]:
                ar[j],ar[j-1]=ar[j-1],ar[j]
    return ar
l=[5,6,1,3,2]
print(bubble_sort(l))
def pivot_position(list1,first, last):
    pivot=list1[first]
    left=first+1
    right=last
    while True:
        while left<=right and list1[left]<=pivot:
            left+=1
        while left<=right and list1[right]>=pivot:
            right-=1
        if right<left:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[first],list1[right]=list1[right],list1[first]
    return right
def quick_sort(list1,first,last):
    if first<last:
        p=pivot_position(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)
    return list1
list1=[56,26,93,17,31,44]
n=len(list1)
print(quick_sort(list1,0,n-1))


def pivot_finding(list2,first,last):
    pivot=list2[first]
    left=first+1
    right=last
    while True:
        while left<=right and list2[left]<=pivot:
            left+=1
        while left<=right and list2[right]>=pivot:
            right-=1
        if right<left:
            break
        else:
            list2[left],list2[right]=list2[right],list2[left]
    list2[first],list2[right]=list2[right],list2[first]

    if left<right:
        p=pivot_finding(list2,first,last)
        pivot_finding(list2,first,p-1)
        pivot_finding(list2,p+1,last)
    return list2
print(pivot_finding([6,1,7,3,8],0,4))

