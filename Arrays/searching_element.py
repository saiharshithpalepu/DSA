from array import *

arr1=array('i',[1,2,3,4,5])

def linearSearch(array,target):
    for i in range(len(array)):
        if(array[i]==target):
            return i
    return -1
        
print(linearSearch(arr1,4))