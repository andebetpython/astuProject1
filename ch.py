import random
def modify(strings,k):
    for i in range(k):
        m=random.choice(strings)
        n=random.choice("ABCDEFGHI")
        new_strings=strings.replace(m,n)
    return new_strings
st="andebet"
print(modify(st,4))
    
