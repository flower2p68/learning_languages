def menor_preco_a_pagar(N, precos):
    # Ordenar os preços em ordem decrescente
    precos.sort(reverse=True)

    # Inicializar o preço total
    preco_total = 0

    # Agrupar os chocolates em grupos de três e calcular o preço total
    for i in range(0, N, 3):
        grupo = precos[i:i+3]
        preco_total += sum(grupo) - max(grupo)

    return preco_total

# Ler o número de chocolates escolhidos
N = int(input())

# Ler os preços dos chocolates
precos = [int(input()) for _ in range(N)]

# Calcular o menor preço a pagar
menor_preco = menor_preco_a_pagar(N, precos)

# Imprimir o menor preço a pagar
print(menor_preco)



















