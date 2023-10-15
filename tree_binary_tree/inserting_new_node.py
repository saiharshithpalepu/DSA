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

new_bt=TreeNode('drinks')
hot=TreeNode('hot')
cold=TreeNode('cold')
new_bt.leftChild=hot
new_bt.rightChild=cold
tea=TreeNode('tea')
coffee=TreeNode('coffee')
hot.leftChild=tea
hot.rightChild=coffee


def insertNewNode(rootNode,newNode):
    if not rootNode:
        rootNode=newNode 
    else:
        customQueue=Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild=newNode
                return 'successfully inserted'
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild=newNode
                return 'successfully inserted'
            
new_node=TreeNode('cola')
print(insertNewNode(new_bt,new_node))
print(cold.leftChild.data)
            