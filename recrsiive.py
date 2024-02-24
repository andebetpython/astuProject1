def func(x,y):
    if x==0:
        return y
    else:
        return func(x-1,x*y)
print(func(4,2))
def mul(arrray):
    maximum=arrray[0]
    if len(arrray)<2:
        maximum=arrray[0]
    else:
         if mul(arrray[1:])>maximum:
             maximum=mul(arrray[1:])
    return maximum
array=[1,4,5,6]
print(mul(array))
a="aaandebet"
b=list(set(a))
k=""
for i in b:
    k+=i
print(k)

