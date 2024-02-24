def sum(nums):
    if nums==1:
        return 1
    return nums+sum(nums-1)
print(sum(5))
pairs=[(1,"one"),(2,"two"),(3,"three"),(4,"four")]
pairs.sort(key=lambda pair:pair[1])
print(pairs)
s="abcde"
print(s.split(("c")))
for a in range(0,2):
    print(a)
    for b in range(0,1):
        print(b)
        for c in range(0,1):
            print(c)