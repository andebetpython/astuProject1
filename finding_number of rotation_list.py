#using linear search
def count_nuber_of_rotation(numbers):
    position=0
    while position<len(numbers):
        if position>0 and numbers[position]<numbers[position-1]:
            return position
        position+=1
    return 0
arr=[4,5,6,1,2,3]
print(count_nuber_of_rotation(arr))
#using binary search
def using_binary_search(array):
    left=0
    right=len(array)-1
    while left<=right:
        mid=len(array)//2
        if array[mid]<array[mid-1] and mid>0:
            return mid
        elif array[mid]<array[len(array)-1]:
            right =mid-1
        else:
            left=mid+1
    return -1
print(using_binary_search(arr))
#finding a target in rotated list
def find_target(rotted_array,target):
    left = 0
    right = len(rotted_array) - 1
    while left <= right:
        mid = len(rotted_array) // 2
        if rotted_array[mid] ==target and mid > 0:
            return mid
        elif rotted_array[mid] < rotted_array[len(rotted_array) - 1]:
            right = mid - 1
        else:
            left = mid + 1
rotated=[5,6,9,0,2,3,4]
print(find_target(rotated,2))
