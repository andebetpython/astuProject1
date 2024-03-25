def group_anagram(list1):
    list2=[]
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if sorted(list1[i])==sorted(list1[j]):
                list2.append([list1[j]])
            else:
                list2.append([list1[i]])
    return list2
s=["ate","eat","tea","dog","god"]
print(group_anagram(s))
