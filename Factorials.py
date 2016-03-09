from functools import reduce
from math import e as E
from math import pi as PI
from math import log
import decimal
from Rationals import rational
# Similar to summation,
# but multiplies instead of adds (capital PI)
def productSequence(m,n,rule=(lambda n: n),inc=1):
    res = 1
    while m <= n:
        res = res * rule(m)
        print("{0} : {1}".format(str(res),m))
        m += inc
    return res
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
def kthFactorial(n,k):
    if 0 <= n < k:
        return 1
    else:
        return n * kthFactorial((n-k),k)
def quadrupleFactorial(n):
    return factorial(2*n) / factorial(n)
def superFactorial(n):
    return productSequence(1,n,factorial)

def processSequence(m,n,
                    oper=(lambda x,y: x+y),
                    baseVal=0,
                    rule=(lambda n: n),
                    inc=(lambda n: n+1)):
    while m <= n:
        baseVal = oper(baseVal,rule(m))
        print("{1} : {0}".format(baseVal.value()*4,m))
        m = inc(m)
    return baseVal
def machin(n):
    a = rational(pow(-1,n),(2*n+1))
    b = rational(1,5)
    b = b.power(2*n+1)
    b = b.multiply(rational(4,1))
    c = rational(1,239).power(2*n+1)
    return a.multiply(b.subtract(c))
def main():
    # print(productSequence(1,4))
    # print(factorial(4))
    # print(kthFactorial(4,1))
    # print(reduce((lambda x,y: x*y),range(1,4+1)))

    # print(superFactorial(30))
    # print(productSequence(m=a,n=b,rule=r,inc=1))

    decimal.getcontext().prec = 3000
    decimal.getcontext().Emax = 999999999999999999
    a = decimal.Decimal(0)
    b = decimal.Decimal(1E9)
    op = lambda x,y: x.add(y)
    r = lambda x: x
    print(processSequence(m=a,n=b,
                          oper=op,
                          baseVal=rational(0,1),
                          rule=machin))

if __name__ == '__main__':
    main()
