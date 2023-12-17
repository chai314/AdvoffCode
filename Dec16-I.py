# Another fucking shitty problem
import sys as stepsys
stepsys.setrecursionlimit(69*69)

A = []
while (s:=list(input()))!=['$']: A+=[s]
B = [[0]*len(A[0]) for i in range(len(A))]
dejavu = set() 

def prop(x,y,dx,dy): #down x right y
    B[x][y]=1
    if not (0<=x+dx<len(A) and 0<=y+dy<len(A[0])) or (x,y,dx,dy) in dejavu: return
    dejavu.add((x,y,dx,dy))
    if dx==0 and A[x+dx][y+dy]=='|': prop(x+dx,y+dy,-1,0); prop(x+dx,y+dy,1,0); return 
    if dy==0 and A[x+dx][y+dy]=='-': prop(x+dx,y+dy,0,1); prop(x+dx,y+dy,0,-1); return 
    Dx, Dy = dx, dy
    if A[x+dx][y+dy]=='/': Dx,Dy = -dy,-dx
    if A[x+dx][y+dy]=='\\': Dx,Dy = dy,dx
    return prop(x+dx,y+dy,Dx,Dy)

if A[0][0] in ['\\','|']: prop(0,0,1,0)
else: prop(0,0,0,1)

print(sum((sum(i)) for i in B))
