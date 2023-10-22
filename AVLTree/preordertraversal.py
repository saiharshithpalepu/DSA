class AVLTree:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.height=1

new_avl_tree=AVLTree(10)
new_avl_tree.leftChild=AVLTree(5)
new_avl_tree.rightChild=AVLTree(15)

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

preOrderTraversal(new_avl_tree)
