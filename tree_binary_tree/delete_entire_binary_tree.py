class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

new_bt=TreeNode('drinks')
hot=TreeNode('hot')
cold=TreeNode('cold')
new_bt.leftChild=hot
new_bt.rightChild=cold

def deleteBT(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None
    