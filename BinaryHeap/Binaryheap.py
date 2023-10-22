class Heap:
    def __init__(self,size):
        self.customList=[None]*(size+1)
        self.heapSize=0
        self.maxSize=size+1

def peekOfHeap(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.customList[1]
    
def heapSize(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize
    
def levelOrdertraversal(rootNode):
    if not rootNode:
        return 
    else:
        for i in range(1,rootNode.heapSize+1):
            print(rootNode.customList[i])

def heapifyTreeInsert(rootNode,index,heapType):
    parentIndex=int(index/2)
    if index<=1:
        return 
    if heapType=='Min':
        if rootNode.customList[index]<rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index]=rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)
    elif heapType=='Max':
        if rootNode.customList[index]>rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index]=rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)

def insertNode(rootNode,nodeValue,heapType):
    if rootNode.heapSize+1==rootNode.maxSize:
        return 'the binary heap is full'
    rootNode.customList[rootNode.heapSize+1]=nodeValue
    rootNode.heapSize+=1
    heapifyTreeInsert(rootNode,rootNode.heapSize,heapType)

def heapifyTreeExtract(rootNode,index,heapType):
    leftIndex=2*index
    rightIndex=2*index+1
    swapChild=0

    if rootNode.heapSize<leftIndex:
        return
    elif rootNode.heapSize==leftIndex:
        if heapType=='Min':
            if rootNode.customList[leftIndex]<rootNode.customList[index]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
                return
        else:
             if rootNode.customList[leftIndex]>rootNode.customList[index]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
                return
    else:
        if heapType=='Min':
            if rootNode.customList[leftIndex]<rootNode.customList[rightIndex]:
                swapChild=leftIndex
            else:
                swapChild=rightIndex
            if rootNode.customList[swapChild]<rootNode.customList[index]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[swapChild]
                rootNode.customList[swapChild]=temp
        elif heapType=='Max':
            if rootNode.customList[leftIndex]>rootNode.customList[rightIndex]:
                swapChild=leftIndex
            else:
                swapChild=rightIndex
            if rootNode.customList[swapChild]<rootNode.customList[index]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[swapChild]
                rootNode.customList[swapChild]=temp
        heapifyTreeExtract(rootNode,swapChild,heapType)

def extractNode(rootNode,heapType):
    if rootNode.heapSize==0:
        return
    else:
        extractedNode=rootNode.customList[1]
        rootNode.customList[1]=rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize]=None
        rootNode.heapSize-=1
        heapifyTreeExtract(rootNode,1,heapType)
        return extractedNode

def deleteEntireHeap(rootNode):
    rootNode.customList=None 
        
            


new_binary_heap=Heap(5)
print(new_binary_heap.customList)
insertNode(new_binary_heap,3,'Min')
insertNode(new_binary_heap,4,'Min')
insertNode(new_binary_heap,1,'Min')
insertNode(new_binary_heap,2,'Min')
insertNode(new_binary_heap,5,'Min')
levelOrdertraversal(new_binary_heap)
extractNode(new_binary_heap,'Min')
extractNode(new_binary_heap,'Min')
levelOrdertraversal(new_binary_heap)
