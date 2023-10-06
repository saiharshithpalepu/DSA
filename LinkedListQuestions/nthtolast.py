class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

    def __str__(self):
        return str(self.value)
    
class LinkedList:
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
                result+='->'
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
            self.tail=new_node
        self.length+=1

linked_list=LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)
print(linked_list)

def nthtolast(linkedlist,n):
    pointer1=linkedlist.head
    pointer2=linkedlist.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2=pointer2.next

    while pointer2:
        pointer1=pointer1.next
        pointer2=pointer2.next
    return pointer1 

print(nthtolast(linked_list,2))
