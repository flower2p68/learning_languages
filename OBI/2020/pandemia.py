N,M=list(map(int,input().split()))
i,r=list(map(int,input().split()))

infectados=set()

for m in range(1,M+1):
    p=set(map(int,input().split()[1:]))
    if m>=r and i in p:
        infectados  |= p
    elif infectados & p:
        infectados  |= p
print(len(infectados))
    