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
    
    def insert(self,index,value):
        if index<0 or index>=self.length:
            return None
        new_node=Node(value)
        if index==0:
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
        elif index==self.length-1:
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
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
            new_node.next=temp.next
            new_node.prev=temp
            new_node.next.prev=new_node
            temp.next=new_node
        self.length+=1

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

circular_doubly_linked_list=CircularDoublyLinkedList()
circular_doubly_linked_list.append(1)
circular_doubly_linked_list.append(2)
circular_doubly_linked_list.append(3)
circular_doubly_linked_list.append(4)
circular_doubly_linked_list.append(5)
circular_doubly_linked_list.insert(1,22)
print(circular_doubly_linked_list)
