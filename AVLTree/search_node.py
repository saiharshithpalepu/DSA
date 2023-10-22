class AVLTree:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.height=1

new_avl_tree=AVLTree(10)
new_avl_tree.leftChild=AVLTree(5)
new_avl_tree.rightChild=AVLTree(15)

def searchNode(rootNode,nodeValue):
    if rootNode.data==nodeValue:
        print(f'{nodeValue} is found')
    elif nodeValue<rootNode.data:
        if rootNode.leftChild.data==nodeValue:
            print(f'{nodeValue} is found')
        else:
            searchNode(rootNode.leftChild)
    else:
        if rootNode.rightChild.data==nodeValue:
            print(f'{nodeValue} is found')
        else:
            searchNode(rootNode.rightChild)

searchNode(new_avl_tree,5)

            
            