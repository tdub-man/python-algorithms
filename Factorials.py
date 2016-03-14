from functools import reduce
from math import e as E
from math import pi as PI
from math import log
from math import sqrt
import decimal
from Rationals import rational
# Similar to summation
# but multiplies instead of adds (capital PI)
def productSequence(m,n,rule=(lambda n: n),inc=1):
    res = 1
    while m <= n:
        res = res * rule(m)
        # print("{0} : {1}".format(m,str(res)))
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
                    inc=(lambda n: n+1),
                    coeff=1):
    count = 0
    while m <= n:
        baseVal = oper(baseVal,rule(m))
        # print("{0} : {1}".format(m,coeff*baseVal.value()*4))
        print(count)
        count += 1
        m = inc(m)
    return baseVal
def machin(n):
    # Machin Series
    a = rational(pow(-1,n),(2*n+1))
    b = rational(1,5)
    b = b.power(2*n+1)
    b = b.multiply(rational(4,1))
    c = rational(1,239).power(2*n+1)
    return a.multiply(b.subtract(c))
def chudnovsky(n):
    # Chudnovsky's Formula
    num = pow(-1,n) * productSequence(1,6*n) * ((545140134*n)+13591409)
    den = productSequence(1,3*n) * pow(productSequence(1,n),3) * decimal.Decimal.sqrt(pow(640320,3*(2*n+1)))
    # a = rational(pow(-1,n),1)
    # b = rational(productSequence(1,6*n),1)
    # c = rational(1,pow(productSequence(1,n),3)*productSequence(1,3*n))
    # d = rational(13591409+(545140134*n),pow(640320,3*n))
    return rational(num,den)
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
    b = decimal.Decimal(500)
    op = lambda x,y: x.add(y)
    r = lambda x: x
    pi = processSequence(m=a,n=b,
                          oper=op,
                          baseVal=rational(0,1),
                          rule=chudnovsky,
                          coeff=12).value()
    print(pow(12*pi,-1))

if __name__ == '__main__':
    main()
