def diseruim_cheek(number):
    new_num=str(number)
    digit=sum(int(i)**(index+1)for index,i in enumerate(new_num))
    if digit==number:
        return True
    return  False
print(diseruim_cheek(89))
def num_cheek(num1):
    n=str(num1)
    d=sum(int(i)for i in n)
    return num1%d==0
print(num_cheek(18))
def self_deviding(number):
    m=str(number)
    for i in m:
        if number%int(i)!=0:
            return False
    return True
print(self_deviding(36))


