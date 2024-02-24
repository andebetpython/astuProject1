def sub(string1):
    j=0
    list1=[]
    for i in range(len(string1)):
            list1.append(string1[j:i+1])
    print(list1)
print(sub("ababa"))