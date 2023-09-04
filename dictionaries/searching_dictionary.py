my_dict={'name':'edy','age':25,'address':'london'}

def search_dict(dict,value):
    for key in dict:
        if(dict[key]==value):
            return key,value
    return ' the value is not found in dictionary'

print(search_dict(my_dict,25))