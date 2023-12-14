# Another fucking shitty problem
import numpy as np
L = []; ans = 0

def score():
    Z = 0
    for sixtynine,m,A in ((100,L.shape[0],L),(1,L.shape[1],L.T)):
        for i in range(1,2*m-1,2):
            x,y = (i-1)//2, (i+1)//2
            Z += sixtynine*(x+1)* all(all(A[x-j]==A[y+j]) for j in range(min(x,m-y-1)+1))
    return Z
  
# Pad input with an ultimate newline and then '$'
while (s:=list(input()))!=['$']:
    if s: L+=[s]; continue
    L = np.array(L); ans += score(); L = []
print(ans)
