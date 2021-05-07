#!/usr/bin/env python3

# Created by: Nika Zamani
# Created on: April 2021
# This program guesses a number between 0 and 9


import constants


def main():
    # this function guesses a number between 0 and 9

    # input
    player_guess = int(input("Enter the number between 0 - 9: "))

    # process & output
    if player_guess == constants.correct_answer:
        print("You guessed correct!")
        print("")
        print("Done.")

    if player_guess > 5:
        print("You guessed wrong!")
        print("")
        print("Done.")

    if player_guess < 5:
        print("You guessed wrong!")
        print("")
        print("Done.")


if __name__ == "__main__":
    main()
