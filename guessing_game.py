"""
Python Development Techdegree
Project 1 - The Number Guessing Game
Author: Sarah Lorenzen
--------------------------------
"""

# Import the random module.

import random

# Create the start_game function.
# Write your code inside this function.

def start_game():

    best_score = None # Best score to track the lowest number of attempts

    print("----------------------------------------")
    print("----------------------------------------")
    print("Welcome to the Number Guessing Game!") # Welcome message
    print("----------------------------------------")
    print("----------------------------------------")
    print()

    num_solve = random.randint(1, 10) # Winning Number - answer/solution

    attempts = 0 # Number of attempts to guess the winning number

    while True:
                try:
                    num_guess = int(input("Guess a number between 1 and 10: ")) # Prompt for Guess of Number
                    if num_guess < 1 or num_guess > 10: # Checks if number guess is in range
                        raise ValueError("Guess must be between 1 and 10")

                    attempts += 1 # Increment attempts

                    if num_guess > num_solve:
                            print("Nope! It's lower!")
                            print()
                    elif num_guess < num_solve:
                            print("Nope! It's higher!")
                            print()
                    else:
                            print(f"You got it!!! Total Attempts: {attempts}")
                            print()
                            if best_score is None or best_score > attempts:
                                    best_score = attempts
                            break

                except ValueError:
                    if num_guess < 1 or num_guess > 10:
                        print("Oh no! That's not a valid value. Try again...") # Handle invalid input

    if best_score:
            print()
            print(f"Current Best Score: {best_score} attempts") # Display best score if available
            print("----------------------------------------")
            print("----------------------------------------")
            print()

    play_again = input("Would you like to play again? Type Yes or No: ").lower().strip() # Formats input to lowercase and strips whitespace
    if play_again == "yes":
        print()
        print() 
        start_game()
    else:
        print()
        print() 
        print("Thanks for playing! Goodbye!")

# Kick off the program by calling the start_game function.
start_game()