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
            poppedNode=self.linkedlist.head
            self.linkedlist.head=None
            self.linkedlist.tail=None
            return poppedNode
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

class AVLTree:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.height=1

new_avl_tree=AVLTree('drinks')
hot=AVLTree('hot')
cold=AVLTree('cold')
new_avl_tree.leftChild=hot
new_avl_tree.rightChild=cold


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue=Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if(root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

levelOrderTraversal(new_avl_tree)