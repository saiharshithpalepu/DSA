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

    def searchDLL(self,value):
        if self.head is None:
            print('the list does not have any elements')
        else:
            temp=self.head
            while temp is not None:
                if temp.value==value:
                    return f'{temp.value} is in the list'
                temp=temp.next
            return f'{value} is not in the list'
        
doubly_linked_list=DoublyLinkedList()
doubly_linked_list.append(10)
doubly_linked_list.append(20)
doubly_linked_list.append(30)
print(doubly_linked_list.searchDLL(40))

