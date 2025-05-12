#math operacion
operacion = input("Expression:")
#operacion components
x , y, z= operacion.split()
# Who is x and z?
#how i did:
#x=float(x)
#z=float(z)
#intelligent guy:
x,z=float(x), float(z)
#more intelligent one:
#print(f"{eval(operacion):.2f}")

#adicion
if y == "+":
        print(round(x + z,2))
        # other way:
        #print(f"{x+z:.2f}")
#less
elif y == "-":
        print(round(x - z,2))

#times
elif y == "*":
        print(round(x * z, 2))

#divide
elif y == "/":
        print(round(x / z, 2))


    
    