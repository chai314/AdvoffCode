# Another fucking shitty problem
L = input().split(',')
from functools import reduce
ans = sum(reduce(lambda x,i: ((x+ord(i))*17)%256, s, 0) for s in L)
print(ans)
