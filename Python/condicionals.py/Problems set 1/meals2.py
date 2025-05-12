def main():
    time= input("What time is it?")
    time_c=convert(time)
    if   8 >= time_c >=7:
        print("Breakfast time")
    elif 13 >= time_c >=12:
        print("Lunch time")
    elif  19 >= time_c >=18:
        print("Dinner time")
    else:
        print("isn't time to eat") 
def convert(time):
    hours, minutes=time.split(":")
    hours = (int(minutes)/60)+int(hours)
    return(hours)
main()
    