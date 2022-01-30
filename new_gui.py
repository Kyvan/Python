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
                        print (f'{_word1.capitalize()}{randint(1, 9)}{random.choice(string.punctuation)}'
                        f'{_word2.capitalize()}{randint(1, 9)}')


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