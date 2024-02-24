def longest_common_prefix(list1):
    n=len(list1)
    i=0
    min_length=float("inf")
    for s in list1:
        if len(s)<min_length:
            min_length=len(s)
    while i<min_length:
        for s in list1:
            if s[i]!=list1[0][i]:
                return s[:i]
        i+=1
    return list1[0][:i]
l=["flower","flight","flow"]
print(longest_common_prefix(l))