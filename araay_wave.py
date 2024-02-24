def wave_array(array):
    m=len(array)
    for i in range(0,m,2):
        if i<m-1 and array[i]>array[i+1]:
            array[i],array[i+1]=array[i+1],array[i]
        if i<m-1 and array[i]<array[i+1]:
            array[i],array[i+1]=array[i+1],array[i]
    return array
arr=[1,2,6,4,5]
print(wave_array(arr))
def list_dict(lst):
    d={}
    for i in range(0,len(lst),2):
        d[lst[i]]=lst[i+1]
    return d
list1=[1,42,2,35,3,25]
print(list_dict(list1))

def string_man(a,b):
    count=0
    flag=True
    m=1
    while flag:
        x=a*m
        count+=1
        if b in x:
            flag=False
        else:
            m+=1
    return count
print(string_man("abcd","cdabcdab"))
def valid_palindrom(string):
    flag=True
    for i in range(len(string)):
        if flag:
            string.replace(string[i],"")
            if string[::-1]==string:
                return True
        break
string="acba"
print(valid_palindrom(string))
