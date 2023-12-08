# Ghosts are quantum woowoo of course. 
from math import lcm
from functools import reduce
I,d = input(),{}; input()
# Add a '$' at the end, guv'nor
while (s:=input().split())!=['$']: d.update({s[0]:(s[2][1:-1],s[3][:-1])})

answers = []
for s in filter(lambda x: x[-1]=='A', d.keys()):
    ans = 0
    while s[-1]!='Z':
        s = d[s][0] if I[ans%len(I)]=='L' else d[s][1]
        ans += 1
    answers.append(ans)

ans = reduce(lcm, answers)
print(ans)

