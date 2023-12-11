# Another fucking shitty problem

L,g = [],0
# Slap a '$' at the end, guv'nor
while (s:=list(input()))!=['$']: L+=[s]; g+=s.count('#')
n,m = len(L), len(L[0])

galaxies = [] 
for i in range(n): galaxies += [(i,j) for j in range(m) if L[i][j]=='#']
R = ['#' not in L[i] for i in range(n)]
C = [all(L[i][j]!='#' for i in range(n)) for j in range(m)]

ans = 0
for iG1 in range(g):
    for iG2 in range(iG1,g):
        G1,G2 = galaxies[iG1], galaxies[iG2]
        u,x = sorted((G1[0],G2[0])); v,y = sorted((G1[1],G2[1]))
        ans += x+y-u-v+sum(R[u:x])+sum(C[v:y])
print(ans)
