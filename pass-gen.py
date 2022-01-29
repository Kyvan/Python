from random_words import RandomWords
from random import randint
import sys, string, random

rw = RandomWords()

def wordGenerator():
   word1 = rw.random_word(letter=None)
   word2 = rw.random_word(letter=None)
   passPhrase(word1, word2)

def passPhrase(_word1, _word2):
   print (f'{_word1.capitalize()}{randint(1, 9)}{random.choice(string.punctuation)}{_word2.capitalize()}{randint(1, 9)}')

if len(sys.argv) == 2:
   for x in range(int(sys.argv[1])):
      wordGenerator()
else:
   for x in range(5):
      wordGenerator()
