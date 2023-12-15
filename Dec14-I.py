# Unintentionally teetered on a Lovecraftian precipice, this code
import numpy as np
L = []
# Marinate the input
while (s:=list(input()))!=['$']: L=[s[::-1]]+L
L = np.array(L+[list('#'*len(L[0]))]).T

for i in range(len(L)):
    j0 = 0
    for j in range(len(L[0])):
        if L[i,j]=='#': L[i,j0:j] = sorted(L[i,j0:j]); j0 = j+1

ans = sum(sum(j+1 for j in range(len(L[0])) if L[i,j]=='O') for i in range(len(L)))
print(ans)
