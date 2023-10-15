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

    def __iter__(self):
        curr=self.head
        while curr:
            yield curr
            curr=curr.next

class Queue:
    def __init__(self):
        self.linkedlist=LinkedList()

    def __str__(self):
        values=[str(x) for s in self.linkedlist]
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
            return "there are no elements in the linked list"
        elif self.linkedlist.head==self.linkedlist.tail:
            popped_node=self.linkedlist.head
            self.linkedlist.head=None
            self.linkedlist.tail=None
            return popped_node
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
        
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

new_binary_tree=TreeNode('drinks')
hot=TreeNode('hot')
cold=TreeNode('cold')
new_binary_tree.leftChild=hot
new_binary_tree.rightChild=cold

def search_node(rootNode,nodeValue):
    if not rootNode:
        return 
    else:
        customQueue=Queue()
        customQueue.enqueue(rootNode)
        while(not customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.data==nodeValue:
                return "success"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return 'not found'

print(search_node(new_binary_tree,'cola'))

        


