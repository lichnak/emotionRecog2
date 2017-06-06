#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Zde zajišťujeme potřebné importy.
# Základní GUI widgety jsou umístěny v modulu QtGui.
import sys
from PyQt4 import QtCore, QtGui
from test1gui import Ui_MainWindow

class MyForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.helloworld)

    def helloworld(self):
        self.ui.textEdit.setText('Hello world')
        print ('Hello world again')

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
