def list_comp(lst):
    new_list=[i for i in lst if i%2==0]

    return new_list
n=[1,2,3,4,5,6,7,8]
print(list_comp(n))
for i in range(12):
    print(i*12)

def reverse_string(s):
    i=0
    while i<len(s):
        print(s[(len(s)-1)-i],end="")
        i+=1
print(reverse_string("andebet"))