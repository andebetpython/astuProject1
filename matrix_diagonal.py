def mat_diag(matrix):
    sum1=0
    sum2=0
    for i in range(len(matrix)):
        sum1+=matrix[i][i]
        sum2+=matrix[i][len(matrix)-1-i]
    return abs(sum2-sum1)
mat=[[1,2,3],[4,5,6],[9,8,9]]
print(mat_diag(mat))
def arry_even_odd(array):
    if len(array)==0:
        return  []
    first=[array[0]]
    for i in array[1:]:
        if i%2!=first[-1]%2:
            first.append(i)
    return  first
arr=[1,3,2,4,7,8,5]
print(arry_even_odd(arr))
#this program is used to find the product of the array except it self
def product(nums):
    left_product=[]
    for i in range(0,len(nums)):
        if i==0:
            left_product.append(nums[i])
        else:
            left_product.append(left_product[i-1]*nums[i])

    right_product=[]
    j=0
    for i in range(len(nums)-1,-1,-1):
        if i==len(nums)-1:
            right_product.append(nums[i])
        else:
            right_product.append(right_product[j-1]*nums[i])
        j+=1
    right_product=right_product[::-1]
    result=[]
    for i in range(len(nums)):
        if i==0:
            result.append(right_product[i+1])
        elif i==len(nums)-1:
            result.append(left_product[i-1])
        else:
            result.append(left_product[i-1]*right_product[i+1])
    return result
nums=[2,5,3,4]
print(product(nums))
for i in range(1,1):
    print(i)


