# Another fucking shitty problem
seqs,ans = [],0
# Marinate the input with '$'.
while (seq:=input().split())!=['$']: seqs.append([*map(int,seq)])
for seq in seqs:
    cycles,x = 0,seq[-1]
    while len(set(seq[cycles:]))!=1:
        for i in range(len(seq)-1,cycles,-1): seq[i]-=seq[i-1]
        cycles+=1; x+=seq[-1]
    ans += x
print(ans)
