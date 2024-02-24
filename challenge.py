def list_int(lst):
    new_list=[]
    for i in range(len(lst)-1):
        if i >0:
            if lst[i]>lst[i-1]:
                result=lst[i]+lst[i-1]
            else:
                i+=1
                result = lst[i] + lst[i - 1]
            new_list.append(result)

    return new_list
print(list_int([4,6,7,3,9,5,4,1,8,3,2]))