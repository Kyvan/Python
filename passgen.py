from random_words import RandomWords
from random import randint
import random
import string
import sys

rw = RandomWords()


def word_generator():
   word1 = rw.random_word(letter=None)
   word2 = rw.random_word(letter=None)
   pass_phrase(word1, word2)


def pass_phrase(_word1, _word2):
   pass1 = f'{_word1.capitalize()}{randint(1, 9)}{random.choice(string.punctuation)}{_word2.capitalize()}{randint(1, 9)}'
   pass2 = f'{randint(1, 9)}{_word1.capitalize()}{random.choice(string.punctuation)}{_word2.capitalize()}{randint(1, 9)}'
   pass3 = f'{random.choice(string.punctuation)}{_word1.capitalize()}{randint(1, 9)}{_word2.capitalize()}{randint(1, 9)}'
   pass4 = f'{_word1.capitalize()}{random.choice(string.punctuation)}{randint(1, 9)}{_word2.capitalize()}{randint(1, 9)}'
   pass5 = f'{_word1.capitalize()}{random.choice(string.punctuation)}{_word2.capitalize()}{randint(1, 9)}{randint(1, 9)}'
   pass6 = f'{_word1.capitalize()}{randint(1, 9)}{_word2.capitalize()}{randint(1, 9)}{random.choice(string.punctuation)}'
   pass7 = f'{_word1.capitalize()}{randint(1, 9)}{random.choice(string.punctuation)}{randint(1, 9)}{_word2.capitalize()}'
   pass8 = f'{_word1.capitalize()}{randint(1, 9)}{randint(1, 9)}{random.choice(string.punctuation)}{_word2.capitalize()}'
   pass9 = f'{_word1.capitalize()}{_word2.capitalize()}{randint(1, 9)}{random.choice(string.punctuation)}{randint(1, 9)}'

   passwords = [pass1, pass2, pass3, pass4, pass5, pass6, pass7, pass8, pass9]
   print (random.choice(passwords))


if len(sys.argv) == 2:
   for x in range(int(sys.argv[1])):
      word_generator()
else:
   for x in range(5):
      word_generator()
