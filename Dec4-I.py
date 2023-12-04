halve_me = 0
# Tack on a '$' at the end, guv'nor
while (s:=input())!='$':
    X,Y = s.split('|')
    X = X.split()[2:]
    Y = Y.split()
    score = 0
    for i in Y: score += i in X
    if score: halve_me += 2**score
print(halve_me//2)
