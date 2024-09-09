# program to whether the number is power of 4

def isPowerOfTwo(n):
    if n<=0:
        return False
    if n==1:
        return True
    if n%4 != 0:
        return False
    return isPowerOfTwo(n//4)

n = int(input())
print(isPowerOfTwo(n))
