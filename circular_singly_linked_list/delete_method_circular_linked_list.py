class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class CSLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def __str__(self):
        current=self.head
        result=''
        while current is not None:
            result+=str(current.value)
            current=current.next
            if current==self.head:
                break
            result+='->'
        return result
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        self.length+=1

    def get(self,index):
        
        if(index<-1 or index>=self.length):
            return None
        elif index==-1:
            return self.tail
        else:
            current=self.head
            for _ in range(index):
                current=current.next
        
            return current
        
    def pop_first(self):
        if self.length==0:
            return None
        elif self.length==1:
            popped_node=self.head
            self.head=None
            self.tail=None
        else:
            popped_node=self.head
            self.head=self.head.next
            self.tail.next=self.head
            popped_node.next=None
        self.length-=1
        return popped_node
    
    def pop(self):
        if self.length==0:
            return None
        elif self.length==1:
            popped_node=self.tail
            self.head=None
            self.tail=None
        else:
            popped_node=self.tail
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            temp.next=self.head
            self.tail=temp
            popped_node.next=None
            self.length-=1
            return popped_node
        
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        elif index==self.length-1:
            return self.pop()
        else:
            prev_node=self.get(index-1)
            popped_node=prev_node.next
            prev_node.next=popped_node.next
            popped_node.next=None
            self.length-=1
            return popped_node
        
    def delete_all(self):
        if self.length==0:
            return
        self.tail.next=None
        self.head=None
        self.tail=None

        

cs_linked_list=CSLinkedList()
cs_linked_list.append(10)
cs_linked_list.append(20)
cs_linked_list.append(30)
cs_linked_list.append(40)
print(cs_linked_list)
cs_linked_list.delete_all()
print(cs_linked_list)





            
