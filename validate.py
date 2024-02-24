def validate_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if len(stack)==0 or mapping[char] != stack.pop():
                return False
    return len(stack) == 0
# Test the function
test_string = "([])"
if validate_parentheses(test_string):
    print("Parentheses are valid")
else:
    print("Parentheses are not valid")

def is_balanceed(parente):
    stack=[]
    pairs={"(":")","{":"}","[":"]"}
    for i in parente:
        if i in pairs:
            stack.append(i)
        elif len(stack)==0 or pairs[stack.pop()]!=i:
            return False
    return len(stack)==0
print(is_balanceed("({[()]})"))

a=[1,2,3]
print(a.pop(a[1]))
class Person:
    def __init__(self,age):
        self.age=age
print(Person(12).age)
for i in range(2):
    for j in range(2):
        if (i+j)%2==0:
            print(i+j)
tupple=(1)
print(type(tupple))