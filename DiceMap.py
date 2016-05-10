from random import randint
from functools import reduce
from itertools import product
from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement as combos
from Sequences import productSequence

# Roll three dice
# Map result to rolling one or two dice

def factorial(n):
    return productSequence(1,n)
def sumRange(numDice):
    return (numDice, numDice*6, numDice*6 - numDice + 1)
def diceRoll():
    return (randint(1,6) for i in range(0,3))
def toOneDice(roll):
    return 6 if sum(roll)%6 == 0 else sum(roll)%6
def toTwoDice(roll):
    pass

roll = list(diceRoll())
# print("Roll: {0} | Sum: {1}".format(roll,sum(roll)))
# print("One Dice Map: {0}".format(toOneDice(roll)))

numDice = 2
# print("Sum Range: {0}".format(sumRange(numDice)))

# -------------------------------------------------------
# Probabilities stuff
# -------------------------------------------------------

perm = list(combos(range(1,7),3))
def findTotalCombos():
    # for SUM in range(3,19):
    #     print(sum([len(set(permutations(s))) for s in filter((lambda x: sum(x)==SUM),perm)]))
    a = [sum([len(set(permutations(s))) for s in filter((lambda x: sum(x)==SUM),perm)]) for SUM in range(3,19)]
    return a
stat = findTotalCombos()
# statM = map((lambda x: 6 if x%6 == 0 else x%6),stat)
# dist = list(reduce((lambda x,y: (x[0],x[1]+y[1])),zip(statM,stat)))
sumMod11 = [x%11+2 for x in range(3,19)]

def listToDict(list):
    # Takes list of tuples of size 2
    # Uses first element of each tuple as key
    # Adds the other elements to the value
    keys = set([x[0] for x in list])
    d = dict([(x,0) for x in keys])
    for x in list:
        d[x[0]] += x[1]
    return d
modProb = listToDict(zip(sumMod11,stat))
# print(modProb)
for x,y in modProb.items():
    print("{0}: {1}".format(x,100*y/216.0))
