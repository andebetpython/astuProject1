def max_sum(ll,k):
    pont2=0
    for i in range(0,len(ll)-k+1):
        pont2=max(pont2,sum(ll[i:i+k]))
    return pont2
l=[1,2,3,4,5,6,7]
print(max_sum(l,3))
def brutforce(list2,k1):
    mx=0
    for i in range(len(list2)-k1+1):
        sum=0
        for j in range(i,i+k1):
            sum+=list2[j]
        mx=max(mx,sum)
    return mx
t=[1,2,3,4,5,6,7]
print(brutforce(t,3))
def soltion_two(list4,constant):
    if constant>len(list4):
        return 0
    total=sum(list4[:constant])
    maxsum=total
    for i in range(len(list4)-constant):
        total-=list4[i]
        total+=list4[i+constant]
        maxsum=max(maxsum,total)
    return maxsum
print(soltion_two(t,3))




#number of occurance of a sub string in a string
def sub_str(string,sub_string):
    count=0
    for i in range(len(string)-len(sub_string)+1):
            if string[i:i+len(sub_string)]==sub_string:
                count+=1

    return count
print(sub_str("ANDEBETAND",'AND'))
def longes(name):
    lo=0
    p=0
    list1=[]
    if len(name)==len(set(name)):
        return len(name)
    else:
        for i in range(len(name)):
            if name[i] not in list1:
                list1.append(name[i])
            else:
                lo=max(lo,len(list1[p:i]))
                p=i
        return lo
print(longes("astugonder"))
list1=[40,10,20,30]
list2=sorted(list1)
list3=[]
for i in list1:
    if i in list2:
        list3.append(list2.index(i)+1)
print(list3)


def palindromine(string):
    last=len(string)-1
    first=0
    while first<last:
        if string[first]!=string[last]:
            return False
        first+=1
        last-=1
    return True
st="AABBAA"
print(palindromine(st))
def reversing(list222):
    if len(list222)==0:
        return ""
    return list222[len(list222)-1]+reversing(list222[0:len(list222)-1])
c="hello"
print(reversing(c))
nums=range(1,1000)
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

p=list(filter(is_prime,nums))
#print(p)








