class Stack:
    def __init__(self):
        self.list=[]

    def __str__(self):
        if self.list is not None:
            values=[str(x) for x in reversed(self.list)]
            return '\n'.join(values)
        else:
            return str(None)
    
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
        
    def push(self,value):
        self.list.append(value)
        return ' the element is successfully pushed into the stack'
    
    def pop(self):
        if self.isEmpty() :
            return 'there is no element in the stack'
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return 'there is no element in the stack'
        else:
            return self.list[len(self.list)-1]
        
    def delete(self):
        self.list=None

stack1=Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
print(stack1)
stack1.pop()
print(stack1)
print(stack1.peek())
stack1.pop()
stack1.pop()
stack1.pop()
print(stack1)
stack1.push(1)
print(stack1)
stack1.delete()
print(stack1)

