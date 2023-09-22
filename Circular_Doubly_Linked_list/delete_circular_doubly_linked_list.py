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
        while temp:
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
            self.head.prev=new_node
        self.length+=1

    def deleteNode(self,index):
        if self.head is None:
            print('there is no node in the list')
        else:
            if index==0:
                if self.head==self.tail:
                    self.head.next=None
                    self.head.prev=None
                    self.head=None
                    self.prev=None
                else:
                    self.head=self.head.next
                    self.head.prev=self.tail
                    self.tail.next=self.head
            elif index==self.length-1:
                if self.head==self.tail:
                    self.head.next=None
                    self.head.prev=None
                    self.tail=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=self.head
                    self.head.prev=self.tail
            else:
                current=self.head
                for _ in range(index-1):
                    current=current.next
                current.next=current.next.next
                current.next.prev=current
            self.length-=1

circular_doubly_linked_list=CircularDoublyLinkedList()
circular_doubly_linked_list.append(10)
circular_doubly_linked_list.append(20)
circular_doubly_linked_list.append(30)
circular_doubly_linked_list.append(40)
circular_doubly_linked_list.append(50)
print(circular_doubly_linked_list)
circular_doubly_linked_list.deleteNode(1)
print(circular_doubly_linked_list)
    