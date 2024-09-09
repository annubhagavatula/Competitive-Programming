# program to whether the number is power of 3

def isPowerOfTwo(n):
    if n<=0:
        return False
    if n==1:
        return True
    if n%3 != 0:
        return False
    return isPowerOfTwo(n//3)

n = int(input())
print(isPowerOfTwo(n))
