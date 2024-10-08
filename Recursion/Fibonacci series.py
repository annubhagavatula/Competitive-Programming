# program to find the fibonacci number of the given index

def fib(n):
    if n == 1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

n = int(input())
print(fib(n))

# python can have only maximum of 1000 recursive calls
#so in order to find fibonacci series of larger numbers, we can import sys
# sys.setrecursionlimit(10**6)

#Sample Code:
"""def fib(self, n: int) -> int:
    def recursive(n):
        if n<=1:
            return n
        return recursive(n-1)+recursive(n-2)
    k = recursive(n)
    return k """
