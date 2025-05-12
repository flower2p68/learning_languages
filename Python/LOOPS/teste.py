def main():
    x=int(input("What's x?"))
    if is_even(x):
        print("This number is even")
    else:
     print("This number is odd")
def is_even(n):
    return n %2==0
main()