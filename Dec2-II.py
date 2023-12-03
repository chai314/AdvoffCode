ans = 0
# Tack a $ at the end, guv'nor
while (s:=input())!='$':
   s = s.split()
   ix = int(s[1][:-1])
   r,g,b=0,0,0
   for i in range(2,len(s)-1,2):
      cnt = int(s[i])
      col = s[i+1]
      if col[0]=='r': r = max(r,cnt)
      if col[0]=='g': g = max(g,cnt)
      if col[0]=='b': b = max(b,cnt)   
   ans += r*g*b
print(ans)
