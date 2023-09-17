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

    def __str__(self):
        temp=self.head
        result=''
        while temp is not None:
            result+=str(temp.value)
            if(temp.next is not None):
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


    def insert(self,value,index):
        new_node=Node(value)
        if(index<0 or index>=self.length):
            return False
        elif(self.length==0):
            self.head=new_node
            self.tail=new_node
        elif(index==0):
            new_node.prev=None
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        else:
        
            temp=self.head 
            for _ in range(index-1):
                temp=temp.next
            new_node.prev=temp
            new_node.next=temp.next
            temp.next.prev=new_node
            temp.next=new_node
        self.length+=1


        



    
doubly_linked_list=DoublyLinkedList()
doubly_linked_list.append(10)
doubly_linked_list.append(30)
doubly_linked_list.append(40)
doubly_linked_list.append(50)
print(doubly_linked_list)
doubly_linked_list.insert(20,2)
print(doubly_linked_list)
doubly_linked_list.insert(60,4)
print(doubly_linked_list)
