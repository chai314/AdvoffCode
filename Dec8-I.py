# Another fucking shitty problem
I, d = input(), {}; input()
# Add a '$' at the end, guv'nor
while (s:=input().split())!=['$']: d.update({s[0]:(s[2][1:-1],s[3][:-1])})
ans,s = 0,'AAA'
while s!='ZZZ':
    s = d[s][0] if I[ans%len(I)]=='L' else d[s][1]
    ans += 1
print(ans)
