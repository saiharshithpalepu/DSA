#find the pair of numbers for which their summ will be equal to given number

list1=[1,2,3,2,3,4,5,6]

def givepairOfNumbers(nums,value):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if(nums[i]==nums[j]):
                continue
            elif(nums[i]+nums[j]==value):
                print(i,j)

givepairOfNumbers(list1,6)