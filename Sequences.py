# Similar to summation
# but multiplies instead of adds (capital PI)
def productSequence(m,n,rule=(lambda n: n),inc=1):
    res = 1
    while m <= n:
        res = res * rule(m)
        # print("{0} : {1}".format(m,str(res)))
        m += inc
    return res
# General method for processing a number sequence
# Processes numbers from m to n, incrementing by inc
# oper defines the type of sequence, e.g. product or summation
# baseVal is the starting point of the total, usually not affecting the total,
# e.g. 1 for product sequence or 0 for summation
# rule applies to each number processed, like (Xi)^2
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
        # print(count)
        count += 1
        m = inc(m)
    return baseVal
