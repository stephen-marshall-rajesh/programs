
#Program for user to guess the correct number

import random
print("Hi there What is your name")
name = input()

print("Well " + name +" I am thinking of number between 1 to 20")

secretnumber = random.randint(1,20)

print("Debug: Secretnumber is " + str(secretnumber))
for guesstaken in range(1,7):
    print("Take a guess")
    guess = int(input())

    if guess < secretnumber:
        print("Guess is too low")
    elif guess > secretnumber:
        print("Guess is too high")
    else:
        break # this condition is for correct guess

if guess == secretnumber:
    print("Good Job " + name + "Your guess is correct and you took " + str(guesstaken) + "guesses")
else:
    print("Sorry The Correct number is " + str(secretnumber))

        

