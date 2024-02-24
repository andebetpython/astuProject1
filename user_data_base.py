class UserData:
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email=email

class UserList:
    def __init__(self):
        self.users=[]
    def inserting(self,user):
        i=0
        while i <len(self.users):
            if self.users[i].username>UserData.username:
                break
            i+=1
        self.users.insert(i,UserData)
    def finding_user(self,username):
        for user in self.users:
            if user.username==username:
                return user
    def update(self,user):
        target=self.finding_user(user.username)
        target.username=user.username
        target.email=user.email
        target.name=user.user

    def printing(self):
        return self.users

list=UserList()
list.inserting(["ANDEBET","and","andebettilahun24@gmail.com"])
list.inserting(["astu","adama","@astugmail.com"])
print(list.printing())


