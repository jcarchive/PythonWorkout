import getopt
import sys
import atexit
from random import randint

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

def guess_number(secret_number, base):
    try:
        user_guess = int(input("Input your guess: "), base)
    except ValueError as ve:
        print(f"Sorry that is not a correct integer base {base}.")
        return False

    if user_guess == secret_number:
        print(f"Just right")
        return True
    elif user_guess > secret_number:
        print(f"Too high")
    else:
        print("Too low")
    return False

def getLimits():
    min_value = 1
    max_value = 100
    base = 10
    opts, args = getopt.getopt(sys.argv[1:],"s:e:b:",["--start=","--end=", "--base="])
    for option, value in opts:
        if option == '-b' or option == '--base=':
            if not str.isdigit(value):
                print(f"{value} is not a valid base. Ignoring option")
            else:
                base = int(value)
        if option == '-s' or option == '--start=':
            min_value_str = value;
        elif option == '-e' or option == '--end=':
            max_value_str = value
    try:
        min_value = int(min_value_str, base)
        max_value = int(max_value_str, base)
        return (base, min_value, max_value)
    except ValueError as ve:
        print("There was a format error in the inputs. Falling back to defualts")
        return (10, 1, 100)


def main():
    base, min_value, max_value = getLimits()
    secret_number = randint(min_value, max_value)

    attempts = 1
    while(not guess_number(secret_number, base)):
        print(f"Attempt: {attempts}")
        attempts += 1
    print(f"Game finished in {attempts} attemps.")

main()
