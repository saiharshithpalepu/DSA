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

    def postOrderTraversal(self,index):
        if(self.lastUsedIndex<index):
            return
        self.postOrderTraversal(2*index)
        self.postOrderTraversal(2*index+1)
        print(self.customList[index])

 

new_bt=BinaryTree(8)
new_bt.insertNode('drinks')
new_bt.insertNode('hot')
new_bt.insertNode('cold')
new_bt.insertNode('tea')
new_bt.insertNode('coffee')

new_bt.postOrderTraversal(1)
