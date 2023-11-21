def selectionSort(customList):
    for i in range(0,len(customList)):
        min_index=i
        for j in range(i+1,len(customList)):
            if customList[min_index]>customList[j]:
                min_index=j
        customList[i],customList[min_index]=customList[min_index],customList[i]
    print(customList)

list1=[1,5,4,8,6,9,0,11,7]

selectionSort(list1)