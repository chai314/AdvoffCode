# Another fucking shitty problem
import numpy as np
L = []
ans = 0

def score(mode):
    Z,M = 0,0 # M: Mirror Multiplicity
    sixtynine,n,A = ((100,L.shape[0],L),(1,L.shape[1],L.T))[mode]
    for i in range(1,2*n-1,2):
        x,y = (i-1)//2, (i+1)//2
        if all(all(A[x-j]==A[y+j]) for j in range(min(x,n-y-1)+1)):
            Z += sixtynine*(x+1); M += 1
    return Z, M

def smudge_score(): # cuz return is the ultimate break
    oldS00, oldS10, m, n =  score(0)[0], score(1)[0], L.shape[0], L.shape[1]
    for i in range(m):
        for j in range(n):
            L[i][j] = 1 - L[i][j]
            S00, S01, S10, S11 = *score(0), *score(1)
            if 0<S00!=oldS00: return S00+(1-S01)*oldS00
            if 0<S10!=oldS10: return S10+(1-S11)*oldS10
            L[i][j] = 1 - L[i][j]

# Pad input with an ultimate newline and then '$'
while (s:=list(input().replace('#','1').replace('.','0')))!=['$']:
    if s: L+=[[*map(int,s)]]; continue
    L = np.array(L)
    ans += smudge_score()
    L = []

print(ans)
