#!/home/kyvan/python_env/bin/python
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from random_words import RandomWords
from random import randint
import sys
import string
import random


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        #super(MainWindow, self).__init__(*args, **kwargs)
        super().__init__()

        self.setWindowTitle("My Pass Generator")
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)


        self.setCentralWidget(container)


        button = QPushButton("Press me to generate passwods")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(button)

    def the_button_was_clicked(self, _args):
        rw = RandomWords()


        def word_generator():
           word1 = rw.random_word(letter=None)
           word2 = rw.random_word(letter=None)
           pass_phrase(word1, word2)


        def pass_phrase(_word1, _word2):
           print (f'{_word1.capitalize()}{randint(1, 9)}{random.choice(string.punctuation)}'
            f'{_word2.capitalize()}{randint(1, 9)}')


        for x in range(5):
            word_generator()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
