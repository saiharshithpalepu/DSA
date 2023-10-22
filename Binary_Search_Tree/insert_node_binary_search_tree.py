class BSTNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

def insertNode(rootNode,nodeValue):
    if rootNode.data==None:
        rootNode.data=nodeValue
    elif (nodeValue<=rootNode.data):
        if rootNode.leftChild is None:
            rootNode.leftChild=BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild=BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild,nodeValue)
    return 'the node is successfully inserted'

new_bst=BSTNode(None)
insertNode(new_bst,60)
insertNode(new_bst,70)
insertNode(new_bst,50)
print(new_bst.leftChild.data)