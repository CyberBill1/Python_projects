#!/bin/python3

import random # Importing random library

random_number = random.randint(0, 10) # Creating a random number
guess = 0

while guess != random_number:
    userguess = input("Guess the number i have in mind btwn 0 and 10: ")  # Ask the user to enter any number and store in the userguess variablee

converted_user_guess = int(userguess) # Converting iput userguess to an integer

if random_number == converted_user_guess:   # Check if random number matches with the user's guessed number
    print("It matched")
else:
    print("Better luck next time")