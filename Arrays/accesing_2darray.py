
import numpy as np

twodarr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(twodarr)

def accessElements(array,rowIndex,colIndex):
    if(rowIndex>=len(array) or colIndex>=len(array[0])):
        print('the element is not present in the array')
    else:
        print(array[rowIndex][colIndex])
accessElements(twodarr,2,1)
accessElements(twodarr,3,2)