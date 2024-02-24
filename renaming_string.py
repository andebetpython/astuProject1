def rename_string(old_list,new_list):

    pointer=old_list
    count=0
    i=0
    n=len(old_list)

    while i<n:
        if old_list==new_list:
            count+=1
        else:
            old_list1=old_list.remove(old_list[i])
            if old_list==new_list:
                count+=1
                old_list1=pointer
        i+=1
    return count%10**9+7
print(rename_string(list("ABABA"),list("ABA")))

