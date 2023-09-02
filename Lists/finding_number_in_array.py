import numpy as np

arr1=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

def findnumber(array,number):
    for i in range(len(array)):
        if(array[i]==number):
            print(i)

findnumber(arr1,2)