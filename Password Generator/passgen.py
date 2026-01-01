#!/home/kyvan/python_env/bin/python

import random
import string
import sys
from random_words import RandomWords
from random import randint
from colorama import Fore, Style

rw = RandomWords()
words = []
passwords = []

def error_exit(error_message):
    print(error_message)
    sys.exit(1)

def word_generator(numb_of_words):
    for passes in range(numb_of_words):
        for numb in range(10):
            word = rw.random_word()
            words.append(word.capitalize())

        pass_phrase(words)

def pass_phrase(*args):
    for numb in range(25):
        password = f'{random.choice(words)}{randint(10, 99)}{random.choice(words)}{random.choice(string.punctuation)}{random.choice(words)}{randint(10, 99)}{random.choice(words)}'
        passwords.append(password)

    print (f'{Fore.YELLOW}{random.choice(passwords)}{Style.RESET_ALL}')

def is_integer(user_input):
    try:
        # Attempt to convert the input to an integer
        int(user_input)
        word_generator(int(user_input))
    except ValueError:
        # If a ValueError is raised, the input is not a valid integer
        error_exit("Usage: python3 passGenTest.py [number]")

if len(sys.argv) == 2:
    is_integer(sys.argv[1])
elif len(sys.argv) == 1:
    word_generator(1)
else:
    error_exit("Usage: python3 passGenTest.py [number]")