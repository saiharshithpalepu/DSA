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
            if(current==self.head):
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

    def pop(self):
        if self.length==0:
            return None
        popped_node=self.tail
        if(self.length==1):
            self.head=self.tail=None
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            temp.next=self.head
            self.tail=temp
            popped_node.next=None
        self.length-=1
        return popped_node
    

cs_linked_list=CSLinkedList()
cs_linked_list.append(10)
cs_linked_list.append(20)
cs_linked_list.append(30)
cs_linked_list.append(40)
print(cs_linked_list)
cs_linked_list.pop()
print(cs_linked_list)


