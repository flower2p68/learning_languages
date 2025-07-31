N, F=map(int,input().split())
avanço=set()
for _ in range(1, N+1):
    lava=input().strip()
    linha=""
    for força in lava:
        if int(força) <= F:
            linha += "*"
        else:
            linha += força
        avanço.add(linha)
for lava in avanço:
    print(lava)

        
    

