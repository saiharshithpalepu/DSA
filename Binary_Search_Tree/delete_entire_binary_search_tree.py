class BSTNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

def insertNode(rootNode,node_value):
    if not rootNode.data:
        rootNode.data=node_value
    elif node_value<rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild=BSTNode(node_value)
        else:
            insertNode(rootNode.leftChild,node_value)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild=BSTNode(node_value)
        else:
            insertNode(rootNode.rightChild,node_value)

def deleteBST(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None 

new_bst=BSTNode(None)
insertNode(new_bst,70)
insertNode(new_bst,80)
insertNode(new_bst,60)

