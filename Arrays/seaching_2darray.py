import numpy as np

arr1 =np.array([[1,2,3],[4,5,6],[7,8,9]])

def searchtwodarray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if(array[i][j]==value):
                return 'the value is found at '+str(i)+' '+str(j)+' index'
    return ' the value is not found'

print(searchtwodarray(arr1,5))