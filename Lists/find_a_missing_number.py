#find a missing number

list1=[1,2,3,4,5,6,8,9,10]

def findMissing(arr,n):
    sum1=n*(n+1)/2
    sum2=sum(list1)
    return int(sum1-sum2)

print(findMissing(list1,10))