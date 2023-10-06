def powerofTwo(n):
    if n==0:
        return 1
    else:
        return 2*powerofTwo(n-1)
    
print(powerofTwo(5))