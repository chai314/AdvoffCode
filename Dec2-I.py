ans = 0
while (s:=input())!='$':
   s = s.split()
   ix = int(s[1][:-1])
   r,g,b=0
   for i in range(2,len(s)-1,2):
      cnt = int(s[i])
      col = s[i+1]
      if (cnt>12 and col[0]=='r') or (cnt>13 and col[0]=='g') or (cnt>14 and col[0]=='b'):
         print(s)
         ans+=ix; break
print(ans)
