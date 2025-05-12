s,t,pi=map(int,input().split())
a=[int(i) for i in input().split()]
cam=[]
for _ in range(t):
    cam.append([int(i) for i in input().split()])

pa=0
j=0
r=0
qtd=[]
while j != t*s:
    for i in cam:
        if i==pi:
            if a[cam[i]]>a[cam[i+1]]:
                r+=1
                i=pa
                j+=1
    qtd.append(r)
    r=0
    print(qtd)



