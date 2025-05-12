from collections import deque
ac=[1,0,-1,0]
al=[0,1,0,-1]
l=deque()
n,f=(map(int,input().split()))
m=[]
for _ in range(n):
    m.append(input())
if int(m[0][0])<=f:
    m[0]="*"+ m[0][1:]
    l.append((0,0))
    while l:
        i,j=l.popleft()
    
        for k in range(4):
            a= i + ac[k]
            b= j + al[k]
            if 0 <= a < n and 0 <= b < n:
                if m[a][b]!='*' and int(m[a][b])<=f:
                    m[a]=m[a][:b]+'*'+ m[a][b+1:]
                    l.append((a,b))
for row in m:
    print(row)