class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

newBinaryTree=TreeNode('Drinks')
hot=TreeNode('hot')
cold=TreeNode('cold')
newBinaryTree.leftChild=hot
newBinaryTree.rightChild=cold
tea=TreeNode('tea')
coffee=TreeNode('coffee')
hot.leftChild=tea
hot.rightChild=coffee

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

postOrderTraversal(newBinaryTree)
