class MultiStack:
    def __init__(self,stacksize):
        self.numberOfStacks=3
        self.custList=[0]*(self.numberOfStacks * stacksize)
        self.sizes=[0] * self.numberOfStacks
        self.stacksize=stacksize

    def isFull(self,stacknum):
        if(self.sizes[stacknum]==self.stacksize):
            return True
        else:
            return False
        
    def isEmpty(self,stacknum):
        if(self.sizes[stacknum]==0):
            return True
        else:
            return False
        
    def indexOfTop(self,stacknum):
        offset=stacknum*self.stacksize
        return offset+self.sizes[stacknum]-1
    
    def push(self,item,stacknum):
        if (self.isFull(stacknum)):
            return 'The stack is full'
        else:
            self.sizes[stacknum]+=1
            self.custList[self.indexOfTop(stacknum)]=item


    
    def pop(self,stacknum):
        if(self.isEmpty(stacknum)):
            return 'the stack is Empty'
        else:
            value=self.custList[self.indexOfTop(stacknum)]
            self.custList[self.indexOfTop(stacknum)]=0
            return value
    def peek(self,stacknum):
        if(self.isEmpty(stacknum)):
            return "the stack is empty"
        else:
            value=self.custList(self.indexOfTop(stacknum))
            return value

customStack=MultiStack(6)
print(customStack.isFull(0))
customStack.push(0,1)
print(customStack.sizes)

