def nextpow2(n):
    if n==0:
        return 1
    count = 0
    while( n != 0):
        n >>= 1
        count += 1
    return count