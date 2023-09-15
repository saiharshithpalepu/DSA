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
        temp=self.head
        result=''
        while temp is not None:
            result+=str(temp.value)
            temp=temp.next
            if temp==self.head:
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
        if index<-1 or index>=self.length:
            return None
        elif index==-1:
            return self.tail
        else:
            current =self.head
            for _ in range(index):
                current =current.next
            return current
        
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    
cs_linked_list=CSLinkedList()
cs_linked_list.append(10)
cs_linked_list.append(20)
cs_linked_list.append(30)
cs_linked_list.append(40)
print(cs_linked_list)
cs_linked_list.set_value(1,70)
print(cs_linked_list)