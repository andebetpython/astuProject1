def execeltitle(string):
    size=len(string)
    result=0
    for i in range(size):
        num=ord(string[i])-ord("A")+1
        result=result+num*26**(size-1)
        size-=1
    return result
st="ABBBBB"
print(execeltitle(st))


