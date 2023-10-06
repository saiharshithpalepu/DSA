class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

    def __str__(self):
        return self.value
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def __str__(self):
        temp=self.head
        result=''
        while temp:
            result+=str(temp.value)
            if temp.next is not None:
                result+='->'
            temp=temp.next
        return result
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.next=None
            self.tail=new_node
        self.length+=1

def createLinkedList(min_value,n):
    new_ll=LinkedList()
    for i in range(n):
        new_ll.append(min_value)
        min_value=min_value+1
    return new_ll
    
llA=createLinkedList(1,3)
print(llA)
llB=createLinkedList(4,3)
print(llB)

def sumTwoLists(linkedlist1,linkedlist2):
    n1=linkedlist1.head
    n2=linkedlist2.head
    new_ll=LinkedList()
    carry=0

    while n1 or n2:
        result=carry
        if n1:
            result+=n1.value
            n1=n1.next
        if n2:
            result+=n2.value
            n2=n2.next
        new_ll.append(result%10)
        carry=result//10
    return new_ll

print(sumTwoLists(llA,llB))



            
