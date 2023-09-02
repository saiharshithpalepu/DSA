import numpy as np

twodarray=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(twodarray)

#insert method for 2 d array
newtwodarray=np.insert(twodarray,0,[[17,18,19,20]],axis=1)
print(newtwodarray)

#append method for 2d array

newtwodarray1= np.append(twodarray,[[0,0,0,0]],axis=0)
print(newtwodarray1)
