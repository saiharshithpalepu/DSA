import numpy as np

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)
newarr=np.delete(arr1,0,axis=0)
print(newarr)