list1=[1,2,3,4,5,6,7]
print(list1[0:2])
list1[0:2]=[11,12]
print(list1)

##deleting elements in the list
##pop
list2=['a','b','c','d','e','f']
list2.pop(1)
print(list2)
list2.pop()
print(list2)

##del
list3=['x','y','z','p','q','r']
del list3[0]
print(list3)
del list3[0:3]
print(list3)

##remove method
list4=['a','b','c','d','e','f','a']
list4.remove('a')
print(list4)
