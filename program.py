

def string_min(strings):
    strings=strings.split()
    mininmum=len(strings[0])
    for i in strings:
        if len(i)<mininmum:
            mininmum=i
    return mininmum
print(string_min("my name is andeber from ADDIS"))
def sum_two_element(list,target):
    left=0
    right=len(list)-1
    m=[]
    while left<=right:
        if list[left]+list[right]==target:
            return left,right
            left+=1
            right-=1

        elif list[left]+list[right]<target:
            left+=1
        else:
            right=right-1

    return left,right
print(sum_two_element([1,10,3,4,5,6],11))

