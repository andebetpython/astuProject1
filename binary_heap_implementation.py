class BH:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def adding_node(self,data):
        if self.key is None:
            self.key=data
        elif self.lchild is None:
            self.lchild=BH(data)
            if self.key>self.lchild.key:
                self.key,self.lchild.key=self.lchild.key,self.key
        elif self.rchild is None:
            self.rchild = BH(data)
            if self.key>self.lchild.key:
                self.key,self.rchild.key=self.rchild.key,self.key
        elif self.lchild is not None:
            self.lchild.adding_node(data)
    def travresing_method(self):
        if self.key:
            print(self.key)
            print(self.lchild.key)
            print(self.rchild.key)


bh=BH(100)

l=[10,5,78,9,27]
for i in l:
    bh.adding_node(i)
bh.travresing_method()
