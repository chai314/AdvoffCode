ans = 0
L = []
# Stick a $ at the end of input, guv'nor
while (s:=input())!='$': L.append(s)
L0 = len(L[0])
L1 = len(L)

# Puffy puff puff
puff = '.'*L0
L.insert(0,puff)
L.append(puff)
for i in range(L1):
   L[i] = '.'+L[i]+'.'

sym = ['.','*']
A = [[[] for i in range(L0)] for i in range(L1)]
for i in range(len(L)):
   for j in range(L0):
      num = ""
      if L[i][j] in sym: continue
      if L[i][j-1] in sym:
         k = 0
         while L[i][j+k].isdigit():
            num += L[i][j+k]; k+=1
      if num:
         fucked = False
         for dx in [-1,0,1]:
            for dy in [-1,0,1]:
               for K in range(k):
                  if fucked or j+K+dy>=L0: continue
                  if L[i+dx][j+K+dy] in sym[1:]:
                     A[i+dx][j+K+dy].append(num)
                     fucked = 1

# If num is near * then * is near num
for i in A:
   for j in i:
      if len(j)!=2: continue
      ans += int(j[0])*int(j[1])
print(ans)
