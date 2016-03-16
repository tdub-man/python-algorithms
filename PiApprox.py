from math import e as E
from math import pi as PI
from math import log
from math import sqrt
import decimal
from Rationals import rational
from Sequences import processSequence
from Sequences import productSequence

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
    decimal.getcontext().prec = 3000
    decimal.getcontext().Emax = 999999999999999999
    a = decimal.Decimal(0)
    b = decimal.Decimal(100)
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
