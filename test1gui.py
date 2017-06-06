# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(1147, 711)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(680, 80, 93, 28))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.textSavePath = QtGui.QTextEdit(self.centralwidget)
        self.textSavePath.setEnabled(False)
        self.textSavePath.setGeometry(QtCore.QRect(680, 40, 421, 31))
        self.textSavePath.setObjectName(_fromUtf8("textSavePath"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(770, 80, 93, 28))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.ukladaniLabel = QtGui.QLabel(self.centralwidget)
        self.ukladaniLabel.setGeometry(QtCore.QRect(670, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ukladaniLabel.setFont(font)
        self.ukladaniLabel.setObjectName(_fromUtf8("ukladaniLabel"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(660, 0, 481, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(660, 110, 481, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(650, 10, 20, 111))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1130, 10, 20, 111))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.selectSaveDirButton = QtGui.QPushButton(self.centralwidget)
        self.selectSaveDirButton.setGeometry(QtCore.QRect(1110, 40, 21, 28))
        self.selectSaveDirButton.setObjectName(_fromUtf8("selectSaveDirButton"))
        self.savedPicsNumber = QtGui.QLabel(self.centralwidget)
        self.savedPicsNumber.setGeometry(QtCore.QRect(870, 80, 261, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.savedPicsNumber.setFont(font)
        self.savedPicsNumber.setObjectName(_fromUtf8("savedPicsNumber"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(650, 170, 20, 111))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(660, 270, 481, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(660, 160, 481, 16))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(1130, 170, 20, 111))
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.zpracovaniLabel = QtGui.QLabel(self.centralwidget)
        self.zpracovaniLabel.setGeometry(QtCore.QRect(670, 170, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zpracovaniLabel.setFont(font)
        self.zpracovaniLabel.setObjectName(_fromUtf8("zpracovaniLabel"))
        self.textProcessPath = QtGui.QTextEdit(self.centralwidget)
        self.textProcessPath.setEnabled(False)
        self.textProcessPath.setGeometry(QtCore.QRect(680, 200, 421, 31))
        self.textProcessPath.setObjectName(_fromUtf8("textProcessPath"))
        self.selectProcessDirButton = QtGui.QPushButton(self.centralwidget)
        self.selectProcessDirButton.setGeometry(QtCore.QRect(1110, 200, 21, 28))
        self.selectProcessDirButton.setObjectName(_fromUtf8("selectProcessDirButton"))
        self.preprocessButton = QtGui.QPushButton(self.centralwidget)
        self.preprocessButton.setGeometry(QtCore.QRect(680, 240, 131, 28))
        self.preprocessButton.setObjectName(_fromUtf8("preprocessButton"))
        self.classificationButton = QtGui.QPushButton(self.centralwidget)
        self.classificationButton.setGeometry(QtCore.QRect(820, 240, 131, 28))
        self.classificationButton.setObjectName(_fromUtf8("classificationButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1147, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.startButton.setText(_translate("MainWindow", "Start", None))
        self.textSavePath.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.stopButton.setText(_translate("MainWindow", "Stop", None))
        self.ukladaniLabel.setText(_translate("MainWindow", "Ukladání obrázků", None))
        self.selectSaveDirButton.setText(_translate("MainWindow", "...", None))
        self.savedPicsNumber.setText(_translate("MainWindow", "Ulozeno obrazku: 0", None))
        self.zpracovaniLabel.setText(_translate("MainWindow", "Zpracování obrázků", None))
        self.textProcessPath.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.selectProcessDirButton.setText(_translate("MainWindow", "...", None))
        self.preprocessButton.setText(_translate("MainWindow", "Příprava obrázků", None))
        self.classificationButton.setText(_translate("MainWindow", "Klasifikace emocí", None))

