
time= input("What time is it?")
x,z= time.split(":")      
x,z= int(x), int(z)
time_convert = float((int(z)/60)+ x)
if   8 >= time_convert >=7:
    print("Breakfast time")
elif 13 >= time_convert >=12:
    print("Lunch time")
elif  19 >= time_convert >=18:
    print("Dinner time")
else:
    print("isn't time to eat") 
#def time_convert(x):
    #n,z=x.split(":")
    #n,z= int(n), int(z)
    #return((int(z)/60)+n)
#time_convert= time_convert(time)
#Go to meals2, this is so confusing