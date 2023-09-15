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
        result=''
        temp=self.head
        while temp is not None:
            result+=str(temp.value)
            temp=temp.next
            if(temp.next==self.head):
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
            self.tail=new_node
            new_node.next=self.head
        self.length+=1

    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=new_node
        self.length+=1

    def insert(self,index,value):
        new_node=Node(value)
        if index>self.length or index<0:
            raise Exception('index out of range')
        if index==0:
            if self.head is None:
                self.head=new_node
                self.tail=new_node
                new_node.next=new_node
            else:
                new_node.next=self.head
                self.head=new_node
                self.tail.next=new_node
        elif index==self.length:
            print('step2')
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node 
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
        self.length+=1

cs_linked_list=CSLinkedList()
cs_linked_list.append(10)
cs_linked_list.append(20)
cs_linked_list.append(30)
print(cs_linked_list)
# cs_linked_list.prepend(0)
print(cs_linked_list)
cs_linked_list.insert(1,50)
print(cs_linked_list)

