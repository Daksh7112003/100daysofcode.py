import time
# import time: This line imports the time module, which provides various time-related functions.


t =time.strftime('%H:%M:%S')

# t = time.strftime('%H:%M:%S'): The strftime function is used to format the current time according to the specified format. %H:%M:%S represents the format for hours, minutes, and seconds in 24-hour format. This formatted time string is then assigned to the variable t.



hour = int(time.strftime('%H'))
# hour = int(time.strftime('%H')): This line extracts the current hour from the current time using strftime('%H'), and then converts it to an integer using int(). The result is stored in the variable hour


print(hour)

if(hour>=0 and hour<12):
    print("Good Morning Sir!")
elif(hour>=12 and hour<17):
    print("Good afternoon SIr!")
elif(hour>=17 and hour<24):
    print("Soja bhai ")



