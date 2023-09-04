my_dict1={'one':1,'two':2,'three':3}

print('one' not in my_dict1)
print('two'  in my_dict1)
print(len(my_dict1))

print(all(my_dict1))

my_dict2={1:'one',2:'two',0:'three'}
print(all(my_dict2))

print(any(my_dict2))

my_dict3={0:'one',False:'two'}
print(any(my_dict3))

print(sorted(my_dict1))
