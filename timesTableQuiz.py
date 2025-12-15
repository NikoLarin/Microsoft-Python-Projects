import random

correct = 0

def randXY():
    x = random.randint(1, 20)
    y = random.randint(1, 20)
    return x, y #returns a tuple (x, y) so you need to index this

print("Welcome to the Times Table Quiz!")

questions = int(input("How many questions would you like to answer? "))

for i in range(questions):
    x = randXY()[0] #indexing the tuple to get x 
    y = randXY()[1] #indexing the tuple to get y
    
    answer = x * y
    userAnswer = int(input("What is " + str(x) + " * " + str(y) + "? "))
    
    if userAnswer == answer:
        print("Correct")
        correct += 1
    else:
        print("Incorrect. The answer is", answer)
print("You got " + str(correct) + " out of " + str(questions) + " questions correct.")
print()

grade = (correct / questions) * 100

print("Your grade is: " + str(grade) + "%")
