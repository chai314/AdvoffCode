# 10sec fucking brute force
ans = 0

def valid(t):
    N1 = N.copy()
    s = t+'.'
    for i in range(len(s)):
        if s[i]=='#':
            if N1: N1[0]-=1
            else: return False
        if s[i]=='.' and s[i-1]=='#':
            if N1[0]==0: N1.pop(0)
            else: return False
        if N1 and N1[0]<0: return False
    return N1==[]

def solve(s):
    if '?' in s: return solve(s.replace('?','#',1)) + solve(s.replace('?','.',1))
    return int(valid(s))

# Marinate the input
while (s:=input().split())!=['$']:
    s,*N = s[0], *map(int,s[1].split(','))
    ans+=solve(s)
print(ans)
