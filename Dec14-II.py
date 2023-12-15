# Another fucking shitty problem. Moreover, this solution isn't algorithmic
import numpy as np
L = []
# Marinate the input
while (s:=list('#'+input()+'#'))!=['#','$','#']: L+=[s]
H = [list('#'*len(L[0]))]; L = np.rot90(np.array(H+L+H),-1)
# print(L)

def cycle(L):
    for x in range(4):
        for i in range(len(L)):
            j0 = 0
            for j in range(len(L[0])):
                if L[i,j]=='#': L[i,j0:j] = sorted(L[i,j0:j]); j0 = j+1
        L = np.rot90(L,-1)
    return sum(sum(j for j in range(len(L[0])) if L[i,j]=='O') for i in range(len(L)))
  
from collections import defaultdict
sixtynine = 1000000000
d = defaultdict(list)
for i in range(1,120): # 120-->inf
    d[cycle(L)].append(i)
for i in d.keys():
    if len(d[i])>1 and d[i][0]%14==sixtynine%14: print(i); break
