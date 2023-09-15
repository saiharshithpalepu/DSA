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
        print(2)
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.value)
            if(temp_node.next==self.head):
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

cs_linked_list=CSLinkedList()
print(1)
cs_linked_list.append(10)
cs_linked_list.append(20)
cs_linked_list.append(30)
cs_linked_list.append(40)
print(cs_linked_list)
cs_linked_list.prepend(0)
print(cs_linked_list)
        


