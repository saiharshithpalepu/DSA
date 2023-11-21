import math
def insertionSort(customList):
    for i in range(1,len(customList)):
        current=customList[i]
        j=i-1

        while j>=0 and customList[j]>current:
            customList[j+1]=customList[j]
            j=j-1
        customList[j+1]=current
    return customList

def bucketSort(customList):
    number_of_buckets=round(math.sqrt(len(customList)))
    arr=[]
    max_value=max(customList)

    for i in range(number_of_buckets):
        arr.append([])

    for j in customList:
        index_b=math.ceil(j*number_of_buckets/max_value)
        arr[index_b-1].append(j)

    for i in range(number_of_buckets):
        arr[i]=insertionSort(arr[i])

    k=0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            customList[k]=arr[i][j]
            k+=1
    print(customList)

list1=[5,4,3,8,6,10,9,2,1]
bucketSort(list1)
    