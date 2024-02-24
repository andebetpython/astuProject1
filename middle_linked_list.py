def middle_linked_list():
    length=0
    start=node=head
    while start:
        length+=1
        start=start.ref
    middle=length//2
    counter=0
    while node:
        if counter==middle:
            return node
        else:
            node=node.ref
            counter+=1
            
