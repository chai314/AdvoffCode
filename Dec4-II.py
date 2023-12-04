six = 208
# Tack on a '$' at the end, guv'nor
matches = [0]*six
count = [1]*six
while (s:=input())!='$':
    X,Y = s.split('|')
    X = X.split(); Y = Y.split()
    this = int(X[1][:-1]) - 1
    for i in Y: matches[this] += i in X[2:]

for i in range(six):
    for j in range(matches[i]): count[i+j+1] += count[i]

print(sum(count))
