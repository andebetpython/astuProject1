
def lcm_finding(a,b):
    if a<b:
        grater=b
    else:
        grater=a
    while True:
        if grater%a==0 and grater%b==0:
            return grater
        grater+=1
print(lcm_finding(10,3))
#gcf
def gcf_finding(num1,num2):
    if num1<num2:
        smaller=num1
    else:
        smaller=num2
    while True:
        if num1%smaller==0 and num2%smaller==0:
            return smaller
        if smaller>0:
            smaller-=1
    return "they have no hcf"
print(gcf_finding(17,19))
a="456"
print(list(a))