class BinaryTree:
    def __init__(self,maxSize):
        self.customList=[None]*maxSize
        self.lastUsedIndex=0
        self.maxSize=maxSize

    def insertNode(self,value):
        if self.lastUsedIndex+1==self.maxSize:
            return 'the binary tree is full'
        self.customList[self.lastUsedIndex+1]=value
        self.lastUsedIndex+=1

    def deleteNode(self,nodevalue):
        if self.lastUsedIndex==0:
            return 'there are no nodes in binary tree'
        else:
            for i in range(1,self.lastUsedIndex+1):
                if self.customList[i]==nodevalue:
                    self.customList[i]=self.customList[self.lastUsedIndex]
                    self.customList[self.lastUsedIndex]=None
                    self.lastUsedIndex-=1
                    return "the node has been successfully deleted"
            return 'the node is not found'
        
new_bt=BinaryTree(8)
new_bt.insertNode('drinks')
new_bt.insertNode('hot')
new_bt.insertNode('cold')
new_bt.insertNode('tea')
new_bt.insertNode('coffee')
new_bt.insertNode('cold')
print(new_bt.deleteNode('cold'))
