class AVLTree:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.height=1

new_avl_tree=AVLTree(10)
new_avl_tree.leftChild=AVLTree(5)
new_avl_tree.rightChild=AVLTree(15)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

postOrderTraversal(new_avl_tree)