from random import randint
import timing

# Brute Force Method
def gcd(u,v):
    u = abs(u)
    v = abs(v)
    t = None
    if u < v:
        t = u
    else:
        t = v
    while (u%t != 0) or (v%t != 0):
        t -= 1
    return t
# Euclid's Algorithm With Modulus
def euclidGCD(u,v):
    u = abs(u)
    v = abs(v)
    if (v == 0):
        return u
    else:
        return euclidGCD(v,(u%v))
def euclidGCDnoRecur(u,v):
    u = abs(u)
    v = abs(v)
    while (v != 0):
        t = u%v
        u = v
        v = t
    return u

res = 0
count = 0
goal = 20000
while res <= goal:
    x = randint(1,1E100)
    y = randint(1,1E100)
    # res = euclidGCD(x,y)
    res = euclidGCDnoRecur(x,y)
    count += 1
    print("X: {0}\nY: {1}\nGCD: {2}\nTries: {3}\n{4}".format(x,y,res,count,"-"*104))

#
# if u > v
#   gcd(u and v) = gcd(v and u-v)
#
# gcd(6 and 4) = 2
# gcd(4 and 2) = 2
#
# Subtraction: gcd(39 and 28) = gcd(28 and 11) = gcd(11 and 17) = gcd(11 and 6) = gcd(6 and 5) = gcd(5 and 1) = 1
# Modulus: gcd(39 and 28) = gcd(28 and 11) = gcd(11 and 6) = gcd(6 and 5) = gcd(5 and 1) = 1
