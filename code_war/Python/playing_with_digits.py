def dig_pow(n, p):
    digitos=list(map(int, str(n)))
    soma=0
    k=0
    for i in digitos:
        s=i**p
        soma+=s
        p+=1
    if soma%n==0:
        return(soma/n)
    else:
        return(-1)

print(dig_pow(89,1))      
            


