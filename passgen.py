from random_words import RandomWords
from random import randint
from colorama import Fore, Style
import random
import string
import sys

rw = RandomWords()


def word_generator():
   word1 = rw.random_word(letter=None)
   word2 = rw.random_word(letter=None)
   word3 = rw.random_word(letter=None)
   word4 = rw.random_word(letter=None)
   pass_phrase(word1, word2, word3, word4)


def pass_phrase(_word1, _word2, _word3, _word4):
   pass1 = f'{_word1.capitalize()}{randint(10, 99)}{_word3.capitalize()}{random.choice(string.punctuation)}{_word2.capitalize()}{randint(10, 99)}{_word4.capitalize()}'
   pass2 = f'{randint(10, 99)}{_word1.capitalize()}{_word3.capitalize()}{random.choice(string.punctuation)}{_word2.capitalize()}{randint(10, 99)}{_word4.capitalize()}'
   pass3 = f'{_word3.capitalize()}{random.choice(string.punctuation)}{_word1.capitalize()}{randint(10, 99)}{_word2.capitalize()}{randint(10, 99)}{_word4.capitalize()}'
   pass4 = f'{_word1.capitalize()}{random.choice(string.punctuation)}{_word3.capitalize()}{randint(10, 99)}{_word2.capitalize()}{randint(10, 99)}{_word4.capitalize()}'
   pass5 = f'{_word1.capitalize()}{random.choice(string.punctuation)}{_word2.capitalize()}{randint(10, 99)}{randint(10, 99)}{_word4.capitalize()}'
   pass6 = f'{_word1.capitalize()}{randint(10, 99)}{_word2.capitalize()}{randint(10, 99)}{random.choice(string.punctuation)}{_word4.capitalize()}'
   pass7 = f'{_word1.capitalize()}{randint(10, 99)}{random.choice(string.punctuation)}{randint(10, 99)}{_word2.capitalize()}{_word3.capitalize()}'
   pass8 = f'{_word1.capitalize()}{randint(10, 99)}{randint(10, 99)}{random.choice(string.punctuation)}{_word2.capitalize()}{_word3.capitalize()}'
   pass9 = f'{_word1.capitalize()}{_word2.capitalize()}{randint(10, 99)}{random.choice(string.punctuation)}{randint(10, 99)}{random.choice(string.punctuation)}'

   passwords = [pass1, pass2, pass3, pass4, pass5, pass6, pass7, pass8, pass9]
   print (f'{Fore.YELLOW}{random.choice(passwords)}{Style.RESET_ALL}')


if len(sys.argv) == 2:
   for x in range(int(sys.argv[1])):
      word_generator()
else:
   for x in range(5):
      word_generator()
