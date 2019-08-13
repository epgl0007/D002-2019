from random import randint
integer = randint(1, 100)
number = input("Try to guess the number. \nType a number between 1 to 100.")
if (number < integer):
    input("Your guess is too low")
    guess = guess + 1
elif (number > integer):
    input("Your guess is too high")
    guess = guess + 1
elif (number == integer):
    input("Your gets the number! \n You've guessed %d times" % guess)

if guess == 3:
    print("Sorry, you lose.")
#Imcomplete
