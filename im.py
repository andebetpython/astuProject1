def add_dots(string):
    out_put = ""
    for i in range(len(string)):
        out_put += string[i]
        if i==len(string)-1:
            break
        out_put += "."
    return out_put
print(add_dots("andebnet"))
def remove_dot(dots_string):
    dots_string=dots_string.split()
    for i in range(len(dots_string)):
        if dots_string[i]==".":
            dots_string.pop(dots_string[i])
    return dots_string
print(remove_dot("a.n.d.b.t"))

