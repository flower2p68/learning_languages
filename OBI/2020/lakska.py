a=list(map(int, input().split())) 
k=int(input())
count = a.count(k)
for _ in range(count):
    print("true")

b=a[1:]
print(b)
c = list(input().split())
d = len(c)-1
print(d)
e = int(input())
f = [] 
for i in range(1, e + 1):  
    f.append(i)
    print(f)
M = int(input())
entradas = []

for _ in range(M):
    entrada = input()  
    entradas.append(entrada)  
