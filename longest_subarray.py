def longest_subarry(array):
    new_lit=[]
    for i in range(0,len(array)-1):
        new_lit.append(array[i])
        if i>0 and abs(array[i]-array[i-1])<=1:
            if i>1 and abs(array[i]-array[i-2])<=1:
                new_lit.append(array[i])

    print(new_lit)
    return len(new_lit)
a=[1,2,3,4,5]
print(longest_subarry(a))
#1212