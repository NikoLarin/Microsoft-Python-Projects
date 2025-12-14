import time
import playsound

timer = input("Do you want to set a timer? y/n: ")
while timer == 'y':

    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    totSec = hours * 3600 + minutes * 60 + seconds

    time.sleep(totSec)
    print("Time's up!")
    playsound.playsound('c:\Windows\Media\Ring03.wav')

    timer = input("Do you want to set another timer? y/n: ")
    if timer == 'n':
        print("Goodbye!")