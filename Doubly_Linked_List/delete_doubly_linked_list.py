class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def __str__(self):
        temp=self.head
        result=''
        while temp:
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
            self.tail.next=new_node
            new_node.next=None
            new_node.prev=self.tail
            self.tail=new_node

        self.length+=1

    def deleteNode(self,index):
        if self.head is None:
            print('there is not any element in the list')
            return
        else:
            if index==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=None
            elif index==self.length-1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=None
            else:
                temp=self.head 
                for _ in range(index-1):
                    temp=temp.next
                temp.next=temp.next.next
                temp.next.prev=temp
            self.length-=1


doubly_linked_list=DoublyLinkedList()
doubly_linked_list.append(10)
doubly_linked_list.append(20)
doubly_linked_list.append(30)
doubly_linked_list.append(40)
doubly_linked_list.append(50)
print(doubly_linked_list)
doubly_linked_list.deleteNode(2)
print(doubly_linked_list)
                    

        