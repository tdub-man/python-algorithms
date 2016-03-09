from functools import reduce

tt = str.maketrans({'0':'01','1':'10'})
nth = lambda n : reduce(lambda s, t : s.translate(tt), range(n), '0')
# print(*map(nth, range(6)))
print(nth(4))
