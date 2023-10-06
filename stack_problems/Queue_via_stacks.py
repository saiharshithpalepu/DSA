class Stack:
    def __init__(self):
        self.list=[]

    def __len__(self):
        return len(self.list)

    def push(self,item):
        self.list.append(item)

    def pop(self):
        if self.list==[]:
            return None
        else:
            return self.list.pop()

class QueueViaStack:
    def __init__(self):
        self.inStack=Stack()
        self.outStack=Stack()

    def __str__(self):
        return str(self.inStack.list)

    def enqueue(self,item):
        self.inStack.push(item)

    def dequeue(self):
        while (len(self.inStack)):
            self.outStack.push(self.inStack.pop())
        result=self.outStack.pop()
        while (len(self.outStack)):
            self.inStack.push(self.outStack.pop())

        return result
    
custome_queue=QueueViaStack()
custome_queue.enqueue(1)
custome_queue.enqueue(2)
custome_queue.enqueue(3)
custome_queue.enqueue(4)
print(custome_queue)
print(custome_queue.dequeue())

