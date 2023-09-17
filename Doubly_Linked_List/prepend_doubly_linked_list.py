class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.prev=None
        self.length=0

    def __str__(self):
        temp=self.head
        result=''
        while temp is not None:
            result+=str(temp.value)
            if temp.next is not None:
                result+='-><-'
            temp=temp.next
        return result
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=None
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.prev=None
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1

doubly_linked_list=DoublyLinkedList()
doubly_linked_list.append(10)
doubly_linked_list.append(20)
doubly_linked_list.append(30)
print(doubly_linked_list)
doubly_linked_list.prepend(0)
print(doubly_linked_list)