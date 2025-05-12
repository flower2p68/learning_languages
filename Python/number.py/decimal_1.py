# If want a decimal, use the comand float.
x=float(input("what's x?"))
y=float(input("what's y?"))
z=round(x+y,2)
print(f"{z:,}")
# or the other way is: print(f"{z.2f}), instead of round(x+y,2)
# in Portuguese we use: print(f"{z:.}")
#If u wanna a comma ex:1,000. Use print(f"{z:,}")