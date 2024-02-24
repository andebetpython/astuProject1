def rot_arr(arrr,d):
    count=0
    m=len(arrr)-1
    for i in range(len(arrr)):
        arrr[i],arrr[m-1-i]=arrr[m-1-i],arrr[i]
        count+=1
        if count==d:
            break
    return arrr
arr=[1,2,3,4,5]
print(rot_arr(arr,3))

arrt=[1,2,3,4,5]
