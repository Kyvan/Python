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

def word_generator(number_of_words):
    for numb in range(number_of_words):
        word = rw.random_word()
        words.append(word.capitalize())

    print(words)
    pass_phrase(words)

def pass_phrase(*args):
    for numb in range(100):
        password = f'{random.choice(words)}{randint(10, 99)}{random.choice(words)}{random.choice(string.punctuation)}{random.choice(words)}{randint(10, 99)}{random.choice(words)}'
        passwords.append(password)

    print (f'{Fore.YELLOW}{random.choice(passwords)}{Style.RESET_ALL}')

if len(sys.argv) == 2:
    word_generator(int(sys.argv[1]))
else:
    print("Usage: python3 passGenTest.py <number>")
    sys.exit()