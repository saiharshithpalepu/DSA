class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class CSLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
           self.tail.next=new_node
           new_node.next=self.head
           self.tail=new_node
        self.length+=1

    def traverse(self):
        current=self.head
        while current is not None:
            print(current.value)
            current=current.next
            if(current==self.head):
                break

cs_linked_list=CSLinkedList()
cs_linked_list.append(10)
cs_linked_list.append(20)
cs_linked_list.append(30)
cs_linked_list.append(40)
cs_linked_list.traverse()


