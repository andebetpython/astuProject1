class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def traversing(self):
        if self.head==None:
            print("the linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref


    def adding_bigin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def sum_ll(self):
        sum=0
        n=self.head
        while n:
            sum=sum+n.data
            n=n.ref

        print(sum)
    def find_min(self):
        n=self.head
        minimum=n.data
        while n:
            if minimum>n.data:
                minimum=n.data
            n=n.ref
        print(minimum)
    def find_max(self):
        n=self.head
        maximum=n.data
        while n:
            if maximum<n.data:
                maximum=n.data
            n=n.ref
        print(maximum)

ll=LinkedList()
ll.adding_bigin(100)
ll.adding_bigin(200)
ll.adding_bigin(300)
ll.adding_bigin(900)
ll.sum_ll()
ll.find_min()
ll.find_min()