list1=[10,-20,30,40,-50,-60,70]
new_list=[number for number in list1 if number>0]
print(new_list)
new_list1=[number*number for number in list1 if number<0]
print(new_list1)

sentence='my name is harshith'

def isconsonant(letter):
    vowels='aeiou'
    return letter.isalpha() and letter.islower()  not in vowels

# new_list2=[i for i in sentence if isconsonant(i) ]
# print(new_list2)

list3=[1,-2,-3,-4,-5,6,7,8]
new_list3=[number if number>0 else 0 for number in list3]
print(new_list3)

new_list4=[number if number>0 else 'negtive number' for number in list3]
print(new_list4)

def get_number(number):
    if number>0:
        return number
    else:
        return 'negative number'

new_list5=[get_number(i) for i in list3]
print(new_list5)