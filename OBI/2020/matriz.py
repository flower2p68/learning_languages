# Criando uma matriz 3x3 inicialmente preenchida com zeros
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Alterando a matriz com base em condições
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == j:
            matriz[i][j] = 1
        elif i + j == len(matriz) - 1:
            matriz[i][j] = 2

# Imprimindo a matriz alterada
for linha in matriz:
    print(linha)
