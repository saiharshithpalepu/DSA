#clear method

my_dict1={'name':'edy','age':25,'address':'london','education':'masters'}
print(my_dict1)
my_dict1.clear()
print(my_dict1)

#copy() method

my_dict2={'name':'edy','age':25,'address':'london','education':'masters'}
dict2=my_dict2.copy()
print(my_dict2)
print(dict2)

#fromkeys() method - second parameter is optional

new_dict={}.fromkeys([1,2,3],0)
print(new_dict)
new_dict1={}.fromkeys([1,2,3])
print(new_dict1)

#get() method
my_dict4={'name':'edy','age':25,'address':'london','education':'masters'}
print(my_dict4.get('name','ram'))
print(my_dict4.get('25','ram'))
print(my_dict4.get('25'))
print(my_dict4.get('age'))

#items() method

print(my_dict4.items())

#keys() method

print(my_dict4.keys())

#popitem() method

print(my_dict4.popitem())
print(my_dict4)

#setdefault() method
my_dict5={'name':'edy','age':25,'address':'london','education':'masters'}
print(my_dict5.setdefault('name','added'))
print(my_dict5)
print(my_dict5.setdefault('name1','added'))
print(my_dict5)

#values() method

print(my_dict5.values())

#update() method

new_dict2={'a':1,'b':2,'c':3}
my_dict5.update(new_dict2)
print(my_dict5)

