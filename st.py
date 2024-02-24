def palindrome(string):
    x=""
    for i in string:
        x=i+x
    return x
s="ebe"
if palindrome(s)==s:
    print("true")