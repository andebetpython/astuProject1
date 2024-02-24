def max_product_subarray(array):
    current_max=array[0]
    current_min=array[0]
    privous_max=array[0]
    privous_min=array[0]
    result=array[0]
    for i in range(1,len(array)):
        current_max=max(privous_max*array[i],array[i],privous_min*array[i])
        current_min=min(privous_min*array[i],array[i],privous_min)
        result=max(result,current_max)
        privous_max=current_max
        privous_min=current_min
    return result
c=[-6,4,-5,8,-10,0,8]
print(max_product_subarray(c))
