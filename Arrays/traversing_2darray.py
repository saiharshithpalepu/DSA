import numpy as np

arr1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

def traversingtwodarray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j])
traversingtwodarray(arr1)