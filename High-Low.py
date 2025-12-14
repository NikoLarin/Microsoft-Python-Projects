import random
import time

def chooseNumber():
    randomNum = random.randint(1, 10)
    print("The number is: " + str(randomNum))
    return randomNum

print("This game is called High-Low.")
print()
print("A number between 1 and 10 will be chosen at random.")
print("You have to guess whether the next number will be higher or lower.")
print("If you guess wrong... you're OUT!")
print()

start = input("Are you ready to play? y/n: ")
while start == 'y':
    oldNum = chooseNumber()
    print()
    highLow = input("Will the next number be higher or lower than " + str(oldNum) + "? Type h/l: ")
    time.sleep(5)
    newNum = chooseNumber()
    if newNum > oldNum and highLow == 'h':
        print("You guessed right! Next round.")
        print()
    elif newNum < oldNum and highLow == 'l':
        print("You guessed right! Next round.")
        print()
    elif newNum < oldNum and highLow == 'h':
        print("Sorry, you guessed wrong. You're out!")
        start = 'n'
    elif newNum > oldNum and highLow == 'l':
        print("Sorry, you guessed wrong. You're out!")
        start = 'n'


