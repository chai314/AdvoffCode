# Another fucking shitty problem
from collections import Counter
order, L = 'AKQJT98765432', []

# Add a '$' at the end, guv'nor
while (s:=input())!='$': L.append(s.split())
for i in range(len(L)):
    x = sorted(Counter(L[i][0]).values())
    L[i]=[7]*(x==[5])+[6]*(x==[1,4])+[5]*(x==[2,3])+[4]*(x==[1,1,3])+[3]*(x==[1,2,2])+[2]*(x==[1,1,1,2])+[1]*(x==[1]*5) + L[i]
ans = sum((1+x)*int(y[2]) for x,y in enumerate(sorted(L, key=lambda x: (x[0],tuple(~order.find(i) for i in x[1])))))
print(ans)
