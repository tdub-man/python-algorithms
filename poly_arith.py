from collections import namedtuple
from itertools import product as xzip

def getLists(inputFile):
    listPair = namedtuple('listPair', 'p, q, x1, x2')
    input = open(inputFile)
    p = [float(x) for x in input.readline().split(' ')]
    q = [float(x) for x in input.readline().split(' ')]
    input.readline()
    x1 = [float(x) for x in input.readline().split(' ')]
    x2 = [float(x) for x in input.readline().split(' ')]
    input.close()

    return listPair(p,q,x1,x2)

def polyadd(pairs):
    return [x+y for x,y in zip(pairs.p,pairs.q)]
def polysub(pairs):
    return [x-y for x,y in zip(pairs.p,pairs.q)]
def polymlt(pairs):
    coeffs = [x*y for x,y in xzip(pairs.p,pairs.q)]
    powers = [x+y for x,y in xzip(pairs.x1,pairs.x2)]
    print(powers)
    return [x*y for x,y in xzip(pairs.p,pairs.q)]

lists = getLists('poly_input.txt')

# print(polyadd(lists))
# print(polysub(lists))
print(polymlt(lists))
