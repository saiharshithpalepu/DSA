class Node:
    def __init__(self,value):
        self.value=value
        self.next=None 
        self.prev=Node 

class CircularDoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def __str__(self):
        temp=self.head
        result=''
        while temp is not None:
            result+=str(temp.value)
            if temp.next==self.head :
                break
            result+='-><-'
        return result

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            new_node.prev=new_node

circular_doubly_linked_list=CircularDoublyLinkedList()
circular_doubly_linked_list.append(10)
print(circular_doubly_linked_list)
        