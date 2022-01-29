from random_words import RandomWords
from random import randint
import sys
import string
import random

rw = RandomWords()


def word_generator():
   word1 = rw.random_word(letter=None)
   word2 = rw.random_word(letter=None)
   pass_phrase(word1, word2)


def pass_phrase(_word1, _word2):
   print (f'{_word1.capitalize()}{randint(1, 9)}{random.choice(string.punctuation)}\
{_word2.capitalize()}{randint(1, 9)}')


if len(sys.argv) == 2:
   for x in range(int(sys.argv[1])):
      word_generator()
else:
   for x in range(5):
      word_generator()
