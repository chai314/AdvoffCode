# Another fucking shitty problem
# File-style for some bizarre reason.
import sys as stepsys
stepsys.setrecursionlimit(69*69)
f = open('input.txt','r')
input = lambda: f.readline().strip('\n')

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

ans = 0
def solve(*X):
    global B, dejavu, ans
    B = [[0]*len(A[0]) for i in range(len(A))]
    dejavu = set()
    prop(*X)
    ans = max(ans, sum(sum(i) for i in B))

for i in range(110):
    solve(i,0,0,1)
    solve(0,i,1,0)
    solve(i,109,0,-1)
    solve(109,i,-1,0)
    # Known bug: To hell with mirror on first cell
f.close()

with open ('input.txt','a') as f: f.write(str(ans))
