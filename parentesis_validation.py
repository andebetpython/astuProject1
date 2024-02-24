def par_validation(par):
    stack=[]
    for i in par:
        if i=="(":
            stack.append(i)
        else:
            if len(stack)==0:
                return  False
            else:
                stack.pop()
    return len(stack)==0
a="(()[{]"
print(par_validation(a))

def binarysearch(list1,value):
    left=0
    right=len(list1)-1
    if left<=right:
        middle=(left+right)//2
        if list1[middle]==value:
            return middle
        elif list1[middle]<value:
            binarysearch(list1[middle+1:])
        else:
            binarysearch(list1[:middle])
a=[1,2,3,5]
print(binarysearch(a,2))

