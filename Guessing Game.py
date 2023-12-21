import random

import time, os, sys


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


guess = int(typingInput(
    "Hey, we are playing a guessing game. \nYour job is to guess the number. It is between 1 and 100. \n\nWhat is your guess?: "))

thenumber = random.randint(1, 100)
Guess_count = 1

while guess != thenumber:

    Guess_count += 1

    if guess < thenumber:
        guess = int(typingInput("\nOh too low! Please try again: "))
    else:
        guess = int(typingInput("\nOh too high! Please try again: "))

typingPrint(
    f"\n\n\U0001F525 \U0001F525 \U0001F525 YOU DID IT!!!!! IT ONLY TOOK YOU {Guess_count} GUESSES \U0001F525 \U0001F525 \U0001F525")