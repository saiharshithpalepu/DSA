class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

newBinaryTree=TreeNode('drinks')
hot=TreeNode('hot')
cold=TreeNode('cold')
newBinaryTree.leftChild=hot
newBinaryTree.rightChild=cold

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

inOrderTraversal(newBinaryTree)