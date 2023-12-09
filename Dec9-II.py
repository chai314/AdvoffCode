# Another fucking shitty problem
from functools import reduce
seqs,ans = [],0
# Marinate the input with '$'.
while (seq:=input().split()[::-1])!=['$']: seqs.append([*map(int,seq)])
for seq in seqs:
    X, cycles = [seq[-1]], 0
    while len(set(seq[cycles:]))!=1:
        for i in range(len(seq)-1,cycles,-1): seq[i]=seq[i-1]-seq[i]
        X+=[seq[-1]]; cycles+=1
    ans += reduce(lambda y,x: x-y, X[::-1])
print(ans)
