n = int(input())
num = 0
comandos = [0] * 1000000

for i in range(n):
    x = int(input())
    if x == 0:
        num -= 1
    else:
        comandos[num] = x
        num += 1


total = sum(comandos[:num])
print(total)
