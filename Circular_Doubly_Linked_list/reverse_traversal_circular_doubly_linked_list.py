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
            new_node.prev=self.tail
            new_node.next=self.head
            self.tail=new_node
        self.length+=1

    def reverseTraversal(self):
        if self.head is None:
            print('there are no elements in circular doubly linked list')
        else:
            temp=self.tail
            while temp is not None:
                print(temp.value)
                if (temp==self.head):
                    break
                temp=temp.prev

circular_doubly_linked_list=CircularDoublyLinkedList()
circular_doubly_linked_list.append(10)
circular_doubly_linked_list.append(20)
circular_doubly_linked_list.append(30)
circular_doubly_linked_list.reverseTraversal()

    