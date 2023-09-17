class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def createDLL(self,value):
        new_node=Node(value)
        new_node.next=None
        new_node.prev=None
        self.head=new_node
        self.tail=new_node
        return 'the doubly linked list is created successfully'

        