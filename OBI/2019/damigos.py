n = int(input())
andares= [int(i) for i in input().split()]

dist = 0
k = -1
for i in range(n):
    d = andares[0] + i + andares[i]
    if d > dist:
        dist = d
        k = i

max_dist = 0
for j in range(n):
    if j != k:
        max_dist = max(max_dist, andares[k] + abs(k - j) + andares[j])
print(max_dist)