class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
    
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next

class Queue:
    def __init__(self):
        self.linkedlist=LinkedList()

    def __str__(self):
        values= [str(x) for x in self.linkedlist]
        return ' '.join(values)
    
    def enqueue(self,value):
        new_node=Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head=new_node
            self.linkedlist.tail=new_node
        else:
            self.linkedlist.tail.next=new_node
            self.linkedlist.tail=new_node

    def dequeue(self):
        if self.linkedlist.head is None:
            return 'there is no element in the linked list'
        elif self.linkedlist.head==self.linkedlist.tail:
            self.linkedlist.head=None
            self.linkedlist.tail=None
            return self.linkedlist.head
        else:
            popped_node=self.linkedlist.head
            self.linkedlist.head=self.linkedlist.head.next
            popped_node.next=None
            return popped_node
        
    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False

    def peek(self):
        if self.linkedlist.head is None:
            return 'there is not any node present in the list'
        else:
            return self.linkedlist.head

    def delete(self):
        self.linkedlist.head=None
        self.linkedlist.tail=None

customQueue=Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3) 
print(customQueue)
print(customQueue.dequeue() )
print(customQueue)
print(customQueue.peek())
customQueue.delete()
print(customQueue)

    
