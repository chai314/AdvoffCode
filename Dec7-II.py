# Another fucking shitty problem

from collections import Counter
order, L = 'AKQT98765432J', []
# Add a '$' at the end, guv'nor
while (s:=input())!='$': L.append(s.split())

for i in range(len(L)):
    # This fails when J is the most common
    # y = L[i][0]
    # print(Counter(y).most_common())
    # while 'J' in y: y=y.replace('J',Counter(y).most_common()[0][0])
    # x = sorted(Counter(y).values())

    # Better
    J = L[i][0].count('J')
    x = sorted(Counter(L[i][0]).values())
    if 0<J<5: x.remove(J); x[-1]+=J

    L[i]=[7]*(x==[5])+[6]*(x==[1,4])+[5]*(x==[2,3])+[4]*(x==[1,1,3])+[3]*(x==[1,2,2])+[2]*(x==[1,1,1,2])+[1]*(x==[1]*5) + L[i]
ans = sum((1+x)*int(y[2]) for x,y in enumerate(sorted(L, key=lambda x: (x[0],tuple(~order.find(i) for i in x[1])))))
print(ans)

