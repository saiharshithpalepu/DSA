class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

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
            if temp.next==self.head:
                break
            temp=temp.next
            result+='-><-'
        return result
    
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            new_node.next=self.head
            new_node.prev=self.tail 
            self.head.prev=new_node
            self.tail.next=new_node
            self.head=new_node
        self.length+=1

circular_doubly_linked_list=CircularDoublyLinkedList()
circular_doubly_linked_list.prepend(50)
circular_doubly_linked_list.prepend(40)
circular_doubly_linked_list.prepend(30)
circular_doubly_linked_list.prepend(20)
circular_doubly_linked_list.prepend(10)
print(circular_doubly_linked_list)
            

