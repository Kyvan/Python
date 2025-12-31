#!/home/kyvan/python_env/bin/python


import random
import string
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from random_words import RandomWords
from random import randint


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
        rw = RandomWords()

        def word_generator():
            word1 = rw.random_word(letter=None)
            word2 = rw.random_word(letter=None)
            word3 = rw.random_word(letter=None)
            word4 = rw.random_word(letter=None)
            pass_phrase(word1, word2, word3, word4)

        def pass_phrase(_word1, _word2, _word3, _word4):
            pass1 = f'{_word1.capitalize()}{randint(10, 99)}{_word3.capitalize()}{random.choice(string.punctuation)}\
{_word2.capitalize()}{randint(10, 99)}{_word4.capitalize()}'
            pass2 = f'{randint(10, 99)}{_word1.capitalize()}{_word3.capitalize()}{random.choice(string.punctuation)}\
{_word2.capitalize()}{randint(10, 99)}{_word4.capitalize()}'
            pass3 = f'{_word3.capitalize()}{random.choice(string.punctuation)}{_word1.capitalize()}{randint(10, 99)}\
{_word2.capitalize()}{randint(10, 99)}{_word4.capitalize()}'
            pass4 = f'{_word1.capitalize()}{random.choice(string.punctuation)}{_word3.capitalize()}{randint(10, 99)}\
{_word2.capitalize()}{randint(10, 99)}{_word4.capitalize()}'
            pass5 = f'{_word1.capitalize()}{random.choice(string.punctuation)}{_word2.capitalize()}{randint(10, 99)}\
{randint(10, 99)}{_word4.capitalize()}'
            pass6 = f'{_word1.capitalize()}{randint(10, 99)}{_word2.capitalize()}{randint(10, 99)}\
{random.choice(string.punctuation)}{_word4.capitalize()}'
            pass7 = f'{_word1.capitalize()}{randint(10, 99)}{random.choice(string.punctuation)}{randint(10, 99)}\
{_word2.capitalize()}{_word3.capitalize()}'
            pass8 = f'{_word1.capitalize()}{randint(10, 99)}{randint(10, 99)}{random.choice(string.punctuation)}\
{_word2.capitalize()}{_word3.capitalize()}'
            pass9 = f'{_word1.capitalize()}{_word2.capitalize()}{randint(10, 99)}{random.choice(string.punctuation)}\
{randint(10, 99)}{random.choice(string.punctuation)}{_word4.capitalize()}'

            passwords = [pass1, pass2, pass3, pass4, pass5, pass6, pass7, pass8, pass9]
            print(random.choice(passwords))

        for x in range(10):
            word_generator()

    @QtCore.pyqtSlot()
    def the_simple_button_was_clicked(self):
        rw = RandomWords()

        def word_generator():
            word1 = rw.random_word(letter=None)
            word2 = rw.random_word(letter=None)
            pass_phrase(word1, word2)

        def pass_phrase(_word1, _word2):
            pass1 = f'{_word1.capitalize()}{randint(10, 99)}{_word2.capitalize()}{random.choice(string.punctuation)}'
            pass2 = f'{random.choice(string.punctuation)}{_word1.capitalize()}{randint(10, 99)}{_word2.capitalize()}'
            pass3 = f'{_word2.capitalize()}{random.choice(string.punctuation)}{_word1.capitalize()}{randint(10, 99)}'
            pass4 = f'{randint(10, 99)}{_word2.capitalize()}{random.choice(string.punctuation)}{_word1.capitalize()}'
            pass5 = f'{_word1.capitalize()}{_word2.capitalize()}{randint(10, 99)}{random.choice(string.punctuation)}'
            pass6 = f'{random.choice(string.punctuation)}{_word1.capitalize()}{_word2.capitalize()}{randint(10, 99)}'
            pass7 = f'{randint(10, 99)}{random.choice(string.punctuation)}{_word1.capitalize()}{_word2.capitalize()}'
            pass8 = f'{random.choice(string.punctuation)}{randint(10, 99)}{_word1.capitalize()}{_word2.capitalize()}'
            pass9 = f'{_word2.capitalize()}{random.choice(string.punctuation)}{randint(10, 99)}{_word1.capitalize()}'

            passwords = [pass1, pass2, pass3, pass4, pass5, pass6, pass7, pass8, pass9]
            print(random.choice(passwords))

        for x in range(10):
            word_generator()

    @QtCore.pyqtSlot(str)
    def on_my_stream_message(self, message):
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
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
