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

def searchNode(rootNode,node_value):
    if rootNode.data==node_value:
        print('the value is found')
    elif node_value<rootNode.data:
        if rootNode.leftChild.data==node_value:
            print('the value is found')
        else:
            searchNode(rootNode.leftChild,node_value)
    else:
        if rootNode.rightChild.data==node_value:
            print('the value is found')
        else:
            searchNode(rootNode.rightChild,node_value)


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
searchNode(new_bst,60)