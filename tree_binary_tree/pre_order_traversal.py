class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

    def preOrderTraversal(self,rootNode):
        if not rootNode:
            return
        print(rootNode.data)
        self.preOrderTraversal(rootNode.leftChild)
        self.preOrderTraversal(rootNode.rightChild)
    
    
newBinaryTree=TreeNode('Drinks')
hot=TreeNode('hot')
cold=TreeNode('cold')
newBinaryTree.leftChild=hot
newBinaryTree.rightChild=cold
newBinaryTree.preOrderTraversal(newBinaryTree)
