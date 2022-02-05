#!/usr/bin/python
from PyQt5 import QtCore, QtGui, QtWidgets

class MyStream(QtCore.QObject):
        message = QtCore.pyqtSignal(str)
        def __init__(self, parent=None):
                super(MyStream, self).__init__(parent)

        def write(self, message):
                self.message.emit(str(message))

class MyWindow(QtWidgets.QWidget):
        def __init__(self, parent=None):
                super(MyWindow, self).__init__(parent)

                self.pushButtonPrint = QtWidgets.QPushButton(self)
                self.pushButtonPrint.setText("Click me for Passwords!!")

                self.pushButtonPrint.clicked.connect(self.the_button_was_clicked)

                self.textEdit = QtWidgets.QTextEdit(self)

                self.layoutVertical = QtWidgets.QVBoxLayout(self)
                self.layoutVertical.addWidget(self.pushButtonPrint)
                self.layoutVertical.addWidget(self.textEdit)

        @QtCore.pyqtSlot()
        def the_button_was_clicked(self):
                from random_words import RandomWords
                from random import randint
                import random, string

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
                        print (random.choice(passwords))



                for x in range(10):
                        word_generator()


        @QtCore.pyqtSlot(str)
        def on_myStream_message(self, message):
                self.textEdit.moveCursor(QtGui.QTextCursor.End)
                self.textEdit.insertPlainText(message)


if __name__ == "__main__":
        import sys
        from PyQt5.QtWidgets import QWidget, QApplication

        app = QtWidgets.QApplication(sys.argv)
        app.setApplicationDisplayName("My Passwords!!")

        main = MyWindow()
        main.show()

        myStream = MyStream()
        myStream.message.connect(main.on_myStream_message)

        sys.stdout = myStream
        sys.exit(app.exec_())