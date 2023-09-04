my_dict={'name':'edy','age':25,'address':'london','education':'masters'}

#method1
print(my_dict)
del my_dict['name']
print(my_dict)

#method2
my_dict1={'name':'edy','age':25,'address':'london','education':'masters'} 
print(my_dict1)
remove_element=my_dict1.pop('name',None)  #if no key is there then it will return none
print(remove_element)
print(my_dict1)

#method3
my_dict3={'name':'edy','age':25,'address':'london','education':'masters'} 
my_dict3.popitem()  #removes the last added key value pair from the dictionary
print(my_dict3)

#method4
my_dict4={'name':'edy','age':25,'address':'london','education':'masters'}
my_dict4.clear() #clears all the key value pairs in the dictionary
print(my_dict4)