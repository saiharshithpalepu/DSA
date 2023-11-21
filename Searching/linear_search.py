def linearSearch(array,value):
    for i in range(len(array)):
        if array[i]==value:
            return i
    return -1

list1=[1,2,3,4,5,6,7]
print(linearSearch(list1,9))