class AVLTree:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.height=1

new_avl_tree=AVLTree(10)
new_avl_tree.leftChild=AVLTree(5)
new_avl_tree.rightChild=AVLTree(15)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

inOrderTraversal(new_avl_tree)
    