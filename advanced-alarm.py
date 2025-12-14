import time
import datetime
import playsound

''' make and alarm clock that tests the day of the week
    the alarm will ring at 5am on weekdays and 6am on weekends
    the alarm will play a different sound for weekdays and weekends
    the alarm will play a unique sound for your birthday
'''
onOff = input("Do you want to turn on the alarm? y/n: ")

if onOff == 'n': # NO ALARM
    print("Alarm is off. Goodbye!")

bDay = input("Enter your birthday (MM-DD): ")

while onOff == 'y':
    todayDate = datetime.date.isoweekday(datetime.date.today()) #find todays day
    timeNow = time.localtime() # get current time

    if time.localtime().tm_hour == 5 and todayDate in [1, 2, 3, 4, 5]:  # Weekdays at 5am
        playsound.playsound('c:\Windows\Media\Ring03.wav')

    elif time.localtime().tm_hour == 6 and todayDate in [6, 7]:  # Weekends at 6am
        playsound.playsound('c:\Windows\Media\chimes.wav')

    elif time.localtime().tm_hour == 7 and bDay == time.strftime("%m-%d", time.localtime()):
        playsound.playsound('c:\Windows\Media\notify.wav')

