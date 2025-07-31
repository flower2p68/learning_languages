def is_even(i):
    return i%2==0
n=int(input())
l=int(input())
if is_even(n) and is_even(l):
    print(1)
elif is_even(n) and is_even(l)==False:
    print(0)
elif is_even(n)==False and is_even(l)==False:
    print(1)
else:
    print(0)

    
    