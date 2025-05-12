def main():
    x=int(input("What's x?"))
    if is_even(x):
        print("even")
    else:
        print("Odd")
def is_even(n):
    #what's gonna do?
   return n%2==0
       #first, i did: if n%2==0:
       #return true
       # every bool question u can do return(afirmattive), without colens. Like it is above.
main()