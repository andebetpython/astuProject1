
def string_mutation(string1,string2):
    count=0
    l=[]
    for i in range(0,len(string1)-1,2):
        l.append(string1[i:i+3])
        count+=1
    return l
strig1="ABCDCDC"
str2="CDC"
print(string_mutation(strig1,str2))

def string_man():
    new_one = "AABNDBETT"
    new_val = []
    for i in range(0,len(new_one)-1,3):
         fg=new_one[i:i+3]

         new_val.append(fg)
    return new_val
print(string_man())








