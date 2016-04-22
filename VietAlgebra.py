from itertools import permutations as perm

s = "{0} + {3} - {5} + (13*{1}/{2}) + 12*{4} +({6}*{7}/{8})"
ANS = 87
test = (3,2,1,5,4,7,9,8,6)

def eq(n):
    return (n[0] + n[3] - n[5] + (13*n[1]/n[2]) + 12*n[4] + (n[6]*n[7]/n[8]))
# print(eq(test))
# print(9 + 6 - 2 + (13*8/7) + (12*5) + (3*1/4))

# Find permutations that give the right answer
# x = filter(lambda x: eq(x)==ANS, list(perm(range(1,10))))
# print(len(x))

# Print the formatted solutions
# y = map(lambda x: s.format(*x), x)
# for n in y:
#     print(n)

# Reorder array
# Normal:   0,1,2,3,4,5,6,7,8 # Supplied array to reorder
# Order:    0,3,5,1,2,4,6,7,8 # New order the elements should be in
# ReIndex:  0,3,4,1,5,2,6,7,8 # Where each element in the supplied array is found in the new order,
#                             # e.g. 1 is found at index 3 and 2 is found at index 4

def reorder(reindex, arr):
    x = sorted(zip(reindex, arr), key=lambda x: x[0])
    return [i[1] for i in x]

# Calling reorder on the reindex will give the new order
reindex = [0,3,4,1,5,2,6,7,8]
invOrder = reorder(reindex, range(9))
print(invOrder)
# Calling reorder on a new order will give the reindex
print(reorder(invOrder, range(9)))

# Reordering and reversing the reorder on a char array
values = list("ABCDEFGHI")
reordered = reorder(reindex, values)
print(reordered)
print(reorder(invOrder, reordered))
