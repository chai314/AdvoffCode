# Another fucking shitty problem
from queue import Queue
L = []
# Marinate the input with '$'.
while (s:=list(input()))!=['$']: L += [['.',*s,'.']]
n,m = len(L), len(L[0])-2
L = [['.']*(m+2)] + L + [['.']*(m+2)]

graph = [[[] for i in range(m+2)] for i in range(n+2)]
def neighbors(i,j):
    ans = []
    # Cuddler
    c, u, d, l, r = L[i][j], (i-1,j), (i+1,j), (i,j-1), (i,j+1)
    Lu, Ld, Ll, Lr = L[i-1][j], L[i+1][j], L[i][j-1], L[i][j+1]
    Us, Ds, Ls, Rs = ['|','F','7'], ['|','L','J'], ['-','F','L'], ['-','J','7']
    UU, DD, LL, RR = [Lu,Us,u], [Ld,Ds,d], [Ll,Ls,l], [Lr,Rs,r]
    def use(*seq):
        for XX in seq:
            if XX[0] in XX[1]: ans.append(XX[2])
    if c=='|': use(UU,DD)
    if c=='-': use(LL,RR)
    if c=='L': use(UU,RR)
    if c=='J': use(UU,LL)
    if c=='7': use(LL,DD)
    if c=='F': use(DD,RR)
    if c=='S': use(UU,DD,LL,RR)
    return ans

for i in range(1,n+1):
    for j in range(1,m+1):
        if L[i][j]=='S': start = (i,j)
        X = neighbors(i,j)
        graph[i][j] += [(i,j) for i,j in X if L[i][j]!='.']

q = Queue(); q.put(start)
visited = [[False]*(n+2) for i in range(m+2)]
D = [[0]*(n+2) for i in range(m+2)]
while not q.empty():
    x,y = q.get()
    visited[x][y] = True
    for i,j in graph[x][y]:
        if not visited[i][j]: q.put((i,j)); D[i][j]=D[x][y]+1

print(max(max(i) for i in D))
# Probably overkill

