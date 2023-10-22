class BSTNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
def insertNode(rootNode,node_value):
    if rootNode.data==None:
        rootNode.data=node_value
    elif (node_value<=rootNode.data):
        if rootNode.leftChild is None:
            rootNode.leftChild=BSTNode(node_value)
        else:
            insertNode(rootNode.leftChild,node_value)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild=BSTNode(node_value)
        else:
            insertNode(rootNode.rightChild,node_value)
new_bst=BSTNode(None)
insertNode(new_bst,70)
insertNode(new_bst,50)
insertNode(new_bst,90)
insertNode(new_bst,30)
insertNode(new_bst,60)
insertNode(new_bst,80)
insertNode(new_bst,100)
insertNode(new_bst,20)
insertNode(new_bst,40)
print('preorder traversal')
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
preOrderTraversal(new_bst)
print('inorder traversal')

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
inOrderTraversal(new_bst)
print('postorder traversal')

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
postOrderTraversal(new_bst)
