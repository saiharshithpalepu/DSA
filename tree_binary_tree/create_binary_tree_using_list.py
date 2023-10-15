class BinaryTree:
    def __init__(self,maxSize):
        self.customList=[None] * maxSize
        self.lastUsedIndex=0
        self.maxSize=maxSize

    def insertNode(self,value):
        if self.lastUsedIndex+1==self.maxSize:
            return "the binary tree is full"
        self.customList[self.lastUsedIndex+1]=value
        self.lastUsedIndex+=1
        return 'the node is successfully inserted'

new_bt=BinaryTree(8)
new_bt.insertNode('drinks')
print(new_bt.insertNode('hot'))
