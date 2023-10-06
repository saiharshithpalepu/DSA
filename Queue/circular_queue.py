class Queue:
    def __init__(self,maxSize):
        self.maxSize=maxSize 
        self.items=self.maxSize * [None]
        self.start= -1
        self.top=-1

    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.top+1==self.start:
            return True
        elif self.start==0 and self.top+1==self.maxSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
        
    def enqueue(self,value):
        if(self.isFull()):
            return "the Queue is full"
        else:
            if self.top+1==self.maxSize:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start=0
                self.items[self.top]=value
            return 'the element is inserted at the end of the queue'
        
    def dequeue(self):
        if(self.isEmpty()):
            return 'There is no element in the queue'
        else:
            firstElement=self.items[self.start]
            start=self.start
            if self.start==self.top:
                self.start=-1
                self.stop=-1
            elif self.start==self.maxSize+1:
                self.start=0
            else:
                self.start+=1
            self.items[start]=None
            return firstElement
        
    def peek(self):
        if self.isEmpty():
            return 'there are no elements present in the queue'
        else:
            return self.items[self.start]
        
    def delete(self):
        self.items=self.maxSize*[None]
        self.start=-1
        self.top=-1


        
        
customQueue=Queue(3)
print(customQueue.isFull())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.top)
customQueue.dequeue()
print(customQueue)
customQueue.delete()
print(customQueue)