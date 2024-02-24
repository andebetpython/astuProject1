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
    def adding_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,target):
        n=self.head
        while n is not None:
            if target==n.data:
                break
            n=n.ref
        if n is None:
            print("the element is not found in the linked list")
        else:
            new_node = Node(data)
            new_node.ref=n.ref
            n.ref = new_node
    def add_before(self,data,target):
        if self.head is None:
            print("the linked list is empty ")
            return
        n=self.head
        if target==n.data:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n is not None:
            if n.ref.data==target:
                break
            n=n.ref
        new_node=Node(data)
        new_node.ref=n.ref
        n.ref=new_node

#inserting an element if the linked list is empty
    def adding_to_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("the linked is not empty")
    def update_ll(self,data,index=0):
        position=0
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.ref=self.head
        else:
            while self.head is not None and position!=index:
                position=position+1
                self.head=self.head.ref
            if self.head is not None:
                self.head.data=data
            else:
                print("the index is not found")
    def traversal_ll(self):
        n=self.head
        while n:
            print(n.data)
            n=n.ref
    def size_of_linked_list(self):
        n=self.head
        count=0
        while n:
            count+=1
            n=n.ref
        return count

ll=LinkedList()
ll.adding_to_empty(1000)
ll.add_before(230,1000)
ll.update_ll(2000,1)
print(ll.size_of_linked_list())
print(ll.traversing())





