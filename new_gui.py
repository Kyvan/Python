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



                for x in range(5):
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