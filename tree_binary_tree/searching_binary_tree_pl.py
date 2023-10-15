class BinaryTree:
    def __init__(self,maxSize):
        self.customList=[None]*maxSize
        self.lastusedIndex=0
        self.maxSize=maxSize

    def insertNode(self,value):
        if self.lastusedIndex+1==self.maxSize:
            return 'the binary tree is full'
        self.customList[self.lastusedIndex+1]=value
        self.lastusedIndex+=1

    def searchNode(self,nodeValue):
        for i in self.customList:
            if i ==nodeValue:
                return 'the node is found'
        return 'the node is not found'
    
new_bt=BinaryTree(8)
new_bt.insertNode('drinks')
new_bt.insertNode('hot')
new_bt.insertNode('cold')
print(new_bt.searchNode('drinks'))