#!/usr/bin/env python3

# created by: Youngjun Kim
# created on: May 2021
# This program checks if guessed number is correct or incorrect


import random

def main():
    # this function checks if guessed number is correct or incorrect
    some_number = random.randint(0, 9) # a number between 0 and 9

    # input
    print("Can you guess the number I choose from 0 to 9?")
    while True:
        integer_as_string = input("Enter the guessed number: ")
        print("")

    # process & output
    try:
        integer_as_number = int(integer_as_string)

        if integer_as_number < 0:
            print("This number is a negative.")
        elif some_number == integer_as_number:
            print("Correct!")
            break
        else:
            print("Incorrect, the number was: {0}".format(some_number))
    except Exception:
        print("That was not valid input.")


if __name__ == "__main__":
    main()
