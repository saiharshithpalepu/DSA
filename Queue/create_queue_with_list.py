class Queue:
    def __init__(self):
        self.items=[]

    def __str__(self):
        values =[str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False
        
    def enqueue(self,value):
        self.items.append(value)
        return "the element is inserted  at the end of the queue"
    
    def dequeue(self):
        if(self.isEmpty()):
            return "there is no element in the queue"
        else:
            return  self.items.pop(0)
        
    def peek(self):
        if (self.isEmpty()):
            return "there is no element in the queue"
        else:
            return self.items[0]
        
    def delete(self):
        self.items=None 
    
customQueue=Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue)
customQueue.dequeue()
print(customQueue)
print(customQueue.peek())

