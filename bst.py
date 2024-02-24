class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def adding_to_empty(self,data):
        new_node=Node(data)
        self.root=new_node
    def traversing(self):
        if self.root is None:
            print("the tree is empty")
        else:
            print(self.root.data)



bst=BST()
bst.adding_to_empty(2000)

bst.traversing()

