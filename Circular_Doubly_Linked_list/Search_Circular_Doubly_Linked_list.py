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
            result+='-><-'
            temp=temp.next
        return result
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            self.tail.next=new_node
            new_node.next=self.head
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1

    def search(self,value):
        if self.head is None:
            print('there is no element in the list')
        else:
            temp=self.head
            while temp:
                if temp.value==value:
                    return f'{value} is in the list'
                if temp==self.tail:
                    return f'{value} is not in the list'
                temp=temp.next

circular_doubly_linked_list=CircularDoublyLinkedList()
circular_doubly_linked_list.append(10)
circular_doubly_linked_list.append(20)
circular_doubly_linked_list.append(30)
print(circular_doubly_linked_list.search(40))