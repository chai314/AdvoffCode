# Put the fun in functional programming
from functools import reduce
inp = lambda: [*map(int,input().split()[1:])]
T, D = inp(), inp()

ans = reduce(lambda i,j: i*j, [*map(lambda i: len([*filter(lambda x: x*(T[i]-x) > D[i], range(T[i]))]), range(len(T)))])
print(ans)
