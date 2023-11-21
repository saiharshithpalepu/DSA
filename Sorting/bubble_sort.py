def bubbleSort(customList):
    for i in range(0,len(customList)-1):
        for j in range(0,len(customList)-i-1):
            if customList[j]>customList[j+1]:
                customList[j],customList[j+1]=customList[j+1],customList[j]
    print(customList)

list1=[1,5,4,8,6,9,0,11,7]

bubbleSort(list1)