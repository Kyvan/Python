#!/home/kyvan/python_env/bin/python

import random
import string
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from random_words import RandomWords
from random import randint

rw = RandomWords()
words = []
passwords_simple = []
passwords_complex = []

def word_generator(numb_of_words):
    for passes in range(numb_of_words):
        for numb in range(10):
            word = rw.random_word()
            words.append(word.capitalize())
        if numb_of_words == 10:
            pass_phrase_simple(words)
        elif numb_of_words == 5:
            pass_phrase_complex(words)

def pass_phrase_simple(*args):
    for numb in range(25):
        password = f'{random.choice(words)}{randint(10, 99)}{random.choice(words)}{random.choice(string.punctuation)}'
        passwords_simple.append(password)

    print(random.choice(passwords_simple))

def pass_phrase_complex(*args):
    for numb in range(25):
        password = f'{random.choice(words)}{randint(10, 99)}{random.choice(words)}{random.choice(string.punctuation)}{random.choice(words)}{randint(10, 99)}{random.choice(words)}'
        passwords_complex.append(password)

    print(random.choice(passwords_complex))


class MyStream(QtCore.QObject):
    message = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyStream, self).__init__(parent)

    def write(self, message):
        self.message.emit(str(message))

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        width = 500
        height = 500
        self.setFixedWidth(width)
        self.setMinimumHeight(height)

        self.setStyleSheet("background-color: black;")

        self.pushButtonPrint = QtWidgets.QPushButton(self)
        self.pushButtonPrint.setText("Complex Passwords!!")
        self.pushButtonPrint.resize(200, 25)
        self.pushButtonPrint.setStyleSheet("QPushButton {"
                                           "background-color : blue;"
                                           "}"
                                           "QPushButton::hover {"
                                           "background-color : green"
                                           "}"
                                           "QPushButton::pressed {"
                                           "background-color : orange"
                                           "}"
                                           )

        self.pushButtonPrint3 = QtWidgets.QPushButton(self)
        self.pushButtonPrint3.setText("simple Passwords!!")
        self.pushButtonPrint3.resize(175, 25)
        self.pushButtonPrint3.move(201, 0)
        self.pushButtonPrint3.setStyleSheet("QPushButton {"
                                            "background-color : green;"
                                            "}"
                                            "QPushButton::hover {"
                                            "background-color : blue"
                                            "}"
                                            "QPushButton::pressed {"
                                            "background-color : orange"
                                            "}"
                                            )

        self.pushButtonPrint2 = QtWidgets.QPushButton(self)
        self.pushButtonPrint2.setText("Click me to exit")
        self.pushButtonPrint2.resize(125, 25)
        self.pushButtonPrint2.move(376, 0)
        self.pushButtonPrint2.setStyleSheet("QPushButton {"
                                            "background-color : red;"
                                            "}"
                                            "QPushButton::hover {"
                                            "background-color : purple"
                                            "}"
                                            "QPushButton::pressed {"
                                            "background-color : yellow"
                                            "}"
                                            )

        self.pushButtonPrint.clicked.connect(self.the_complex_button_was_clicked)
        self.pushButtonPrint3.clicked.connect(self.the_simple_button_was_clicked)
        self.pushButtonPrint2.clicked.connect(self.exit_was_clicked)

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.move(0, 25)
        self.textEdit.resize(500, 525)
        self.textEdit.setStyleSheet("QTextEdit {"
                                    "color : yellow"
                                    "}"
                                    )

    @QtCore.pyqtSlot()
    def exit_was_clicked(self):
        sys.exit(app.exec())

    @QtCore.pyqtSlot()
    def the_complex_button_was_clicked(self):
        word_generator(5)

    @QtCore.pyqtSlot()
    def the_simple_button_was_clicked(self):
        word_generator(10)

    @QtCore.pyqtSlot(str)
    def on_my_stream_message(self, message):
        self.textEdit.moveCursor(QtGui.QTextCursor.MoveOperation.EndOfBlock)
        self.textEdit.insertPlainText(message)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationDisplayName("My Passwords!!")

    main = MyWindow()
    main.show()

    myStream = MyStream()
    myStream.message.connect(main.on_my_stream_message)

    sys.stdout = myStream
    sys.exit(app.exec())
