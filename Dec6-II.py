# Another fucking shitty problem
from math import floor, ceil
inp = lambda: int(''.join(input().split()[1:]))
T, D = inp(), inp()
disc = (T**2-4*D)**0.5
alpha, beta = (T-disc)/2, (T+disc)/2
print(1 - ceil(alpha) + floor(beta))
