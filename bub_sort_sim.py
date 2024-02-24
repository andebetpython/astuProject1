l=[6,4,5,3,2,8]
for j in range(len(l)):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print(l)