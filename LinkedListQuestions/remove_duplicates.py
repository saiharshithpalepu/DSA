class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

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
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(3)
linked_list.append(4)
linked_list.append(4)
linked_list.append(5)
linked_list.append(5)
print(linked_list)

def removeDuplicates(linkedlist):

    current=linkedlist.head
    prev=None

    while current:
        runner=current
        while runner.next:
            if runner.value==current.value:
                runner.next=runner.next.next
            else:
                runner=runner.next
        prev=current
        current=current.next

    linkedlist.tail=prev
    return linkedlist

print(removeDuplicates(linked_list))