from random import randint
import atexit
"""
Instructions
- Write a function ( guessing_game ) that takes no arguments.
- When run, the function chooses a random integer between 0 and 100 (inclusive).
- Then ask the user to guess what number has been chosen.
- Each time the user enters a guess, the program indicates one of the following:
    – Too high
    – Too low
    – Just right
- If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
- The program only exits after the user guesses correctly.
"""

secret_number = randint(1,100)

def exit_handler():
    print(f"Finishing. The secret_number was {secret_number}")

def guess_number(secret_number):
    try:
        user_guess = int(input("Input your guess: "))
    except ValueError as ve:
        print("Sorry that is not a correct integer.")
        return False

    if user_guess == secret_number:
        print(f"Just right")
        return True
    elif user_guess > secret_number:
        print(f"Too high")
    else:
        print("Too low")
    return False

def main():
    atexit.register(exit_handler)
    attempts = 1
    while(not guess_number(secret_number)):
        print(f"Attempt: {attempts}")
        attempts += 1
    print(f"Game finished in {attempts} attemps.")

main()
