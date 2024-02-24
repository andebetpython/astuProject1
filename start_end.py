


def first_position(list1,target):
    left=0
    right=len(list1)-1
    while left<=right:
        mid=(left+right)//2
        if mid>0 and list1[mid]==target and list1[mid-1]<target:
            return mid
        elif list1[mid]<target:
            left=mid+1
        else:
            right=mid-1
z=[1,2,3,3,3,3,3]
print(first_position(z,3))
