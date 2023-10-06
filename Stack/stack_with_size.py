class Stack:
    def __init__(self,maxSize):
        self.list=[]
        self.maxSize=maxSize

    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.list)==self.maxSize:
            return True
        else:
            return False
    
    def push(self,value):
        if (self.isFull()):
            return ' the list is full'
        else:
            self.list.append(value)
            return 'the element is added to the stack'
        
    def pop(self):
        if self.isEmpty():
            return ' the list is empty'
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return ' the list is empty'
        else:
            return self.list[len(self.list)-1]
        
    def delete(self):
        self.list=[]

customStack=Stack(4)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.delete()
print(customStack)