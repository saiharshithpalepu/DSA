def factorial(n):
    assert n>=0 and int(n)==n,'the number must be positive integer only'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)