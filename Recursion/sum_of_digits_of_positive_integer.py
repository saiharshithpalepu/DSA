def sumOfDigits(n):
    assert n>=0 and int(n)==n, 'the number must be positive integer only!'
    if n==0:
        return 0
    else:
        return n%10 + sumOfDigits(n//10)
    
print(sumOfDigits(100))