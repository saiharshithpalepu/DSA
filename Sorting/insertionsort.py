def insertionSort(customList):
    for i in range(1,len(customList)):
        current=customList[i]
        j=i-1
        while j>=0 and customList[j]>current:
            customList[j+1]=customList[j]
            j=j-1
        customList[j+1]=current
    print(customList)

list1=[5,4,3,8,6,10,9,2,1]
insertionSort(list1)