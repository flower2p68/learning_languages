frase=input()
feliz= ")"
triste="("
i=0
k=0
for palavra in frase:
    if palavra==feliz:
        i=i+1
    elif palavra==triste:
        k=k+1
if k>i:
    print("chateado")
elif i>k:
    print("divertido")
else:
    print("neutro")

