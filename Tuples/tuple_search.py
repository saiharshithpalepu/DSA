new_tuple=['a','b','c','d','e']

#method1
print('a' in new_tuple)
print('f' in new_tuple)

#method2

print(new_tuple.index('a'))

#method3

def search_tuple(p_tuple,element):
    for i in range(len(p_tuple)):
        if(p_tuple[i]==element):
           return  print(f'element is found at {i} index')
    print(f'the element is not found in the tuple')

search_tuple(new_tuple,'b')