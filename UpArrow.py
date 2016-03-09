from math import e as E
from math import pi as PI

# Formal recursive definition of arrow
def upArrow(a=0,n=0,b=0):
    if n==0:
        return a*b
    elif n>=1 and b==0:
        return 1
    else:
        return upArrow(a,n-1,upArrow(a,n,b-1))
def twoArrow(x=0,n=0):
    p=1
    for i in range(1,n+1):
        p = pow(x,p)
    return p
def threeArrow(x=0,n=0):
    p=1
    for i in range(1,n+2):
        p = pow(x,p)
    return p
# More computable arrow definition
def uArrow(base=0,arrow=0,power=0):
    if arrow==0:
        return base*power
    elif power==0:
        return 1
    elif arrow==1:
        return pow(base,power)
    else:
        p=1
        for i in range(1,power+arrow-1):
            p = pow(base,p)
        return p

def main():
    # a = uArrow(base=2,arrow=2,power=5)
    # b = uArrow(base=2,arrow=3,power=4)
    # c = uArrow(base=2,arrow=4,power=3)
    # d = uArrow(base=2,arrow=5,power=2)
    # e = uArrow(base=2,arrow=6,power=1)
    #
    # f = uArrow(base=2,arrow=7,power=0) # Any number raised to 0 = 1
    # g = uArrow(base=2,arrow=0,power=7) # 0 Arrow is multiplication
    # h = uArrow(base=2,arrow=1,power=6) # 1 Arrow is exponentiation
    # print("{0} : {1} : {2}".format(f,g,h))
    # print("A=B=C=D=E ? {0}\nA = {1}".format((a == b == c == d == e),a))

if __name__ == '__main__':
    main()
