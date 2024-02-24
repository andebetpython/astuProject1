def left_rotation(string):
    s=string+string
    for i in range(len(string)):
        for j in range(len(string)):
            print(s[i+j],end="")
        print()
print(left_rotation("ABCD"))
#cheek one string is the rotation of the other string
def cheek_rotation(string1,string2):
    if len(string1)!=len(string2):
        return False
    new_str=string1+string1
    if string2 in new_str:
        return True
print(cheek_rotation("AND","NDA"))

#right rotation
def right_rotation(string):
    s=string+string
    for i in range(len(string)-1,-1,-1):
        for j in range(len(string)-1,-1,-1):
            print(s[i-j],end="")
        print()
print(right_rotation("ABCD"))
