# Another fucking shitty problem
from queue import Queue
L = []
# Remember to marinate the input with '$'.
while (s:=list(input()))!=['$']: L += [['.',*s,'.']]
n,m = len(L), len(L[0])-2
L = [['.']*(m+2)] + L + [['.']*(m+2)]
# Pad bitch boy on each edge

graph = [[[] for i in range(m+2)] for i in range(n+2)]

# Equal parts bad, brilliant, and convoluted. My type.
def neighbors(i,j):
    ans = []
    # Cuddler
    c, u, d, l, r = L[i][j], (i-1,j), (i+1,j), (i,j-1), (i,j+1)
    Lu, Ld, Ll, Lr = L[i-1][j], L[i+1][j], L[i][j-1], L[i][j+1]
    Us, Ds, Ls, Rs = ['|','F','7'], ['|','L','J'], ['-','F','L'], ['-','J','7']
    UU, DD, LL, RR = [Lu,Us,u], [Ld,Ds,d], [Ll,Ls,l], [Lr,Rs,r]
    def LURD(seq):
        for XX in seq:
            if XX[0] in XX[1]: ans.append(XX[2])
            else: return False
        return True
    CMap = ['|', '-', 'L', 'J', '7', 'F']
    LMap = [[UU,DD], [LL,RR], [UU,RR], [UU,LL], [LL,DD], [DD,RR]]
    if c in CMap: LURD(LMap[CMap.index(c)])
    elif c=='S': L[i][j] = next(CMap[LMap.index(XX)] for XX in LMap if LURD(XX))
    return ans
# Aesthetic. Also swaps S for the right symbol

for i in range(1,n+1):
    for j in range(1,m+1):
        if L[i][j]=='S': start = (i,j)
        X = neighbors(i,j)
        graph[i][j] += [(i,j) for i,j in X if L[i][j]!='.']

q = Queue(); q.put(start)
visited = [[False]*(m+2) for i in range(n+2)]
D = [[0]*(m+2) for i in range(n+2)]
while not q.empty():
    x,y = q.get()
    visited[x][y] = True
    for i,j in graph[x][y]:
        if not visited[i][j]: q.put((i,j)); D[i][j]=D[x][y]+1
# (TW) Width First Search

x,y = start
D[x][y]=69

ans = 0
for i in range(1,n+1):
    mode, prev = 0, 'pebble brain, stubble rash'
    for j in range(1,m+1):
        c = L[i][j]
        if D[i][j]>0:
            if c=='|' or [prev,c] in [['L','7'],['F','J']]: mode=1-mode
            if c!='-': prev = c
        ans+= mode*(D[i][j]==0)

print(ans)
