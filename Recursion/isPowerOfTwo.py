# program to whether the number is power of 2

def isPowerOfTwo(n):
    if n<=0:
        return False
    if n==1:
        return True
    if n%2 != 0:
        return False
    return isPowerOfTwo(n//2)

n = int(input())
print(isPowerOfTwo(n))
