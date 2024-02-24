import  time
start=time.time()
def linear_search(lst,target):
    for i in range(len(lst)-1):
        if lst[i]==target:
            return i

m=[1,2,3,4,5]

end=time.time()
print(end)
print(end-start)

print(linear_search(m,4))