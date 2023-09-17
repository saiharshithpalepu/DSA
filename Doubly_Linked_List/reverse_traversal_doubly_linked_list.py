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
        result=''
        temp=self.head
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
           new_node.next=None
           self.tail.next=new_node
           new_node.prev=self.tail
           self.tail=new_node
        self.length+=1

    def reverseTraversal(self):
        if self.head is None:
            print('there is no element in the list')
        else:
            temp=self.tail
            while temp is not None:
                print(temp.value)
                temp=temp.prev

doubly_linked_list=DoublyLinkedList()
doubly_linked_list.append(10)
doubly_linked_list.append(20)
doubly_linked_list.append(30)
doubly_linked_list.append(40)
doubly_linked_list.append(50)
print(doubly_linked_list)
doubly_linked_list.reverseTraversal()





    