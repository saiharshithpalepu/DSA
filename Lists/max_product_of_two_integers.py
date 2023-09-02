arr1=[1,2,3,4,5,6,7,8,9]

def returnmaxProduct(nums):
    max1=0 #first maximum
    max2=0 #second maximum

    for i in nums:

        if(i>max1):
            max2=max1
            max1=i
        elif(i>max2):
            max2=i 
    return max2 * max1
print(returnmaxProduct(arr1))
