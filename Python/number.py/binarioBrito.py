x = int(input())
u_milhar = 1 * 2**3
centena = (x% 2)*2**2
dezena = ((x//2) % 2)*2**1
unidade = (((x//2)//2) % 2)*2**0
print(u_milhar + centena + dezena + unidade)
print(u_milhar, centena, dezena, unidade)