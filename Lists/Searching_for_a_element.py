
#searching a element

list1=[1,2,3,4,5,6,7,8]
target=2

def in_search(plist,target):
    if(target in plist):
        print(f'{target} is in the list')
    else:
        print(f'{target} is not in the list')

in_search(list1,target)

def linear_search(plist,target):
    for i,value in enumerate(plist):
        if(value==target):
            return i
    return -1

linear_search(list1,target)
