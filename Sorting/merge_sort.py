def merge(customList,l,m,r):
    n1=m-l+1
    n2=r-m

    left_array= [0]* n1
    right_array=[0] *n2

    for i in range(0,n1):
        left_array[i]=customList[l+i]

    for j in range(0,n2):
        right_array[j]=customList[m+1+j]

    i=0
    j=0
    k=0

    while i<n1 and j<n2:
        if left_array[i]<=right_array[j]:
            customList[k]=left_array[i]
            i+=1
        else:
            customList[k]=right_array[j]
            j+=1
        k+=1

    while i<n1:
        customList[k]=left_array[i]
        i+=1
        k+=1

    while j<n2:
        customList[k]=right_array[j]
        j+=1
        k+=1

def mergeSort(customList,l,r):
    if l<r:
        m=(l+(r-1))//2
        mergeSort(customList,l,m)
        mergeSort(customList,m+1,r)
        merge(customList,l,m,r)
    return customList


list1=[5,4,3,8,6,10,9,2,1]
print(mergeSort(list1,0,8))