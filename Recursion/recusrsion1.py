def printNumber(n):
    if n<1:
        print('n is less than 1')
    else:
        printNumber(n-1)
        print(n)

printNumber(10)