class MyClass:
    def __init__(self):
        self.__x=1
    def __str__(self):
        return str(self.__x)
print(MyClass())
print("hello,"+"world")