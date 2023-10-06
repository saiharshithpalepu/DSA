class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None

    def __iter__(self):
        curr=self.head
        while curr:
            yield curr
            curr=curr.next

class Stack:
    def __init__(self):
        self.LinkedList=linkedList()

    def __str__(self):
        values=[str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
        
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.LinkedList.head
        self.LinkedList.head=new_node

    def pop(self):
        if self.isEmpty():
            return ' the list is empty'
        else:
            nodeValue=self.LinkedList.head.value
            self.LinkedList.head=self.LinkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():
            return ' the list is empty'
        else:
            nodeValue=self.LinkedList.head.value
            return nodeValue
        
    def delete(self):
        self.LinkedList.head=None

customStack=Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.isEmpty())
print(customStack)



        