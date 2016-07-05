from functools import reduce
from Sequences import productSequence

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

def factorial1(n):
    prod = 1
    while n > 0:
        prod = prod * n
        n = n - 1
    return prod

def kthFactorial(n,k):
    if 0 <= n < k:
        return 1
    else:
        return n * kthFactorial((n-k),k)

def quadrupleFactorial(n):
    return factorial(2*n) / factorial(n)

def superFactorial(n):
    return productSequence(1,n,factorial)

def main():
    print(productSequence(1,4))
    print(factorial(4))
    print(kthFactorial(4,1))
    print(reduce((lambda x,y: x*y),range(1,4+1)))

    a = 1
    b = 10
    r = (lambda x: pow(x,2))
    print(superFactorial(30))
    print(productSequence(m=a,n=b,rule=r,inc=1))

if __name__ == '__main__':
    main()
