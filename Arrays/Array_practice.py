#creating and traversing an array
from array import *

myarray1=array('i',[1,2,3,4,5])

for i in myarray1:
    print(i)
#accessing individual elements through indexes

print('step2')
print(myarray1[3])

#append any value to the array using append method

print('step 3')
myarray1.append(6)
print(myarray1)

#insert value in an array using insert method
print('step 4')
myarray1.insert(0,11)
print(myarray1)

#extend python array using extend() method
print('step 5')
myarr=array('i',[12,13,14])
myarray1.extend(myarr)
print(myarray1)

#add items from th list into the array using fromlist() method

print('step 6')
templist=[21,22,23]
myarray1.fromlist(templist)
print(myarray1)

#remove an element from the array using remove() method

print('step 7')
myarray1.remove(23)
print(myarray1)

#remove last element using pop method

print('step 8')
myarray1.pop()
print(myarray1)

#fetch any element through index using index() method

print('step 9')
print(myarray1.index(21))

#reverse a python array using reverse method
print('step 10')
myarray1.reverse()
print(myarray1)

#get array buffer information through buffer_info() method

print('step 11')
print(myarray1.buffer_info())

#check the number of occurrences of element using count method

print('step 12')
print(myarray1.count(11))

#convert the array to list uing tolist() function
print('step 13')
myarray1.tolist()
print(myarray1.tolist())

#slice elements from the array
print('step 14')
print(myarray1[1:4])