# Another fucking shitty problem
L = input().split(',')
from functools import reduce
shelf = {i:[] for i in range(256)}
def box(s): return reduce(lambda x,i: ((x+ord(i))*17)%256, s, 0)
def f(s): return [i for i,j in enumerate(B) if j[0]==s]
for s in L:
    if '=' in s:
        x,y = s.split('='); B = shelf[box(x)]
        if (u:=f(x)): B[u[0]][1]=y
        else: B.append([x,y])
    if '-' in s:
        B = shelf[box(s[:-1])]
        if (u:=f(s[:-1])): B.pop(u[0])
        
ans = sum(sum((i+1)*(j+1)*int(shelf[i][j][1]) for j in range(len(shelf[i]))) for i in shelf.keys())
print(ans)
