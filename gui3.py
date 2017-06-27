# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui3.ui'
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
        MainWindow.resize(1156, 711)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setEnabled(False)
        self.startButton.setGeometry(QtCore.QRect(680, 120, 93, 28))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.textSavePath = QtGui.QTextEdit(self.centralwidget)
        self.textSavePath.setEnabled(False)
        self.textSavePath.setGeometry(QtCore.QRect(680, 80, 421, 31))
        self.textSavePath.setObjectName(_fromUtf8("textSavePath"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(770, 120, 93, 28))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.ukladaniLabel = QtGui.QLabel(self.centralwidget)
        self.ukladaniLabel.setGeometry(QtCore.QRect(670, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ukladaniLabel.setFont(font)
        self.ukladaniLabel.setObjectName(_fromUtf8("ukladaniLabel"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(660, 40, 481, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(660, 150, 481, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(650, 50, 20, 111))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1130, 50, 20, 111))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.selectSaveDirButton = QtGui.QPushButton(self.centralwidget)
        self.selectSaveDirButton.setGeometry(QtCore.QRect(1110, 80, 21, 28))
        self.selectSaveDirButton.setObjectName(_fromUtf8("selectSaveDirButton"))
        self.savedPicsNumber = QtGui.QLabel(self.centralwidget)
        self.savedPicsNumber.setGeometry(QtCore.QRect(870, 120, 261, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.savedPicsNumber.setFont(font)
        self.savedPicsNumber.setObjectName(_fromUtf8("savedPicsNumber"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(650, 380, 20, 201))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(660, 570, 481, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(660, 370, 481, 16))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(1130, 380, 20, 201))
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.zpracovaniLabel = QtGui.QLabel(self.centralwidget)
        self.zpracovaniLabel.setGeometry(QtCore.QRect(670, 380, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zpracovaniLabel.setFont(font)
        self.zpracovaniLabel.setObjectName(_fromUtf8("zpracovaniLabel"))
        self.textProcessPath = QtGui.QTextEdit(self.centralwidget)
        self.textProcessPath.setEnabled(False)
        self.textProcessPath.setGeometry(QtCore.QRect(680, 410, 421, 31))
        self.textProcessPath.setObjectName(_fromUtf8("textProcessPath"))
        self.selectProcessDirButton = QtGui.QPushButton(self.centralwidget)
        self.selectProcessDirButton.setGeometry(QtCore.QRect(1110, 410, 21, 28))
        self.selectProcessDirButton.setObjectName(_fromUtf8("selectProcessDirButton"))
        self.preprocessButton = QtGui.QPushButton(self.centralwidget)
        self.preprocessButton.setEnabled(False)
        self.preprocessButton.setGeometry(QtCore.QRect(680, 450, 131, 28))
        self.preprocessButton.setObjectName(_fromUtf8("preprocessButton"))
        self.classificationButton = QtGui.QPushButton(self.centralwidget)
        self.classificationButton.setEnabled(False)
        self.classificationButton.setGeometry(QtCore.QRect(680, 540, 131, 28))
        self.classificationButton.setObjectName(_fromUtf8("classificationButton"))
        self.textEditNote = QtGui.QTextEdit(self.centralwidget)
        self.textEditNote.setGeometry(QtCore.QRect(10, 540, 641, 71))
        self.textEditNote.setObjectName(_fromUtf8("textEditNote"))
        self.ukladaniLabel_2 = QtGui.QLabel(self.centralwidget)
        self.ukladaniLabel_2.setGeometry(QtCore.QRect(10, 510, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ukladaniLabel_2.setFont(font)
        self.ukladaniLabel_2.setObjectName(_fromUtf8("ukladaniLabel_2"))
        self.saveNoteButton = QtGui.QPushButton(self.centralwidget)
        self.saveNoteButton.setEnabled(True)
        self.saveNoteButton.setGeometry(QtCore.QRect(544, 620, 111, 31))
        self.saveNoteButton.setObjectName(_fromUtf8("saveNoteButton"))
        self.textEditExperiment = QtGui.QTextEdit(self.centralwidget)
        self.textEditExperiment.setGeometry(QtCore.QRect(660, 10, 481, 31))
        self.textEditExperiment.setObjectName(_fromUtf8("textEditExperiment"))
        self.cameraButton = QtGui.QPushButton(self.centralwidget)
        self.cameraButton.setGeometry(QtCore.QRect(430, 490, 111, 31))
        self.cameraButton.setObjectName(_fromUtf8("cameraButton"))
        self.cameraDisableButton = QtGui.QPushButton(self.centralwidget)
        self.cameraDisableButton.setGeometry(QtCore.QRect(540, 490, 111, 31))
        self.cameraDisableButton.setObjectName(_fromUtf8("cameraDisableButton"))
        self.textClassificationPath = QtGui.QTextEdit(self.centralwidget)
        self.textClassificationPath.setEnabled(False)
        self.textClassificationPath.setGeometry(QtCore.QRect(680, 500, 421, 31))
        self.textClassificationPath.setObjectName(_fromUtf8("textClassificationPath"))
        self.selectClassificationDirButton = QtGui.QPushButton(self.centralwidget)
        self.selectClassificationDirButton.setGeometry(QtCore.QRect(1110, 500, 21, 28))
        self.selectClassificationDirButton.setObjectName(_fromUtf8("selectClassificationDirButton"))
        self.facesStatsNumber = QtGui.QLabel(self.centralwidget)
        self.facesStatsNumber.setGeometry(QtCore.QRect(820, 450, 311, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.facesStatsNumber.setFont(font)
        self.facesStatsNumber.setObjectName(_fromUtf8("facesStatsNumber"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1156, 21))
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
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.stopButton.setText(_translate("MainWindow", "Stop", None))
        self.ukladaniLabel.setText(_translate("MainWindow", "Ukladání obrázků", None))
        self.selectSaveDirButton.setText(_translate("MainWindow", "...", None))
        self.savedPicsNumber.setText(_translate("MainWindow", "Ulozeno obrazku: 0", None))
        self.zpracovaniLabel.setText(_translate("MainWindow", "Zpracování obrázků", None))
        self.textProcessPath.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.selectProcessDirButton.setText(_translate("MainWindow", "...", None))
        self.preprocessButton.setText(_translate("MainWindow", "Rozpoznat obličeje", None))
        self.classificationButton.setText(_translate("MainWindow", "Klasifikovat emoce", None))
        self.ukladaniLabel_2.setText(_translate("MainWindow", "Poznámka", None))
        self.saveNoteButton.setText(_translate("MainWindow", "Uložit poznámku", None))
        self.textEditExperiment.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">experiment</span></p></body></html>", None))
        self.cameraButton.setText(_translate("MainWindow", "Najít kameru", None))
        self.cameraDisableButton.setText(_translate("MainWindow", "Vypnout kameru", None))
        self.textClassificationPath.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.selectClassificationDirButton.setText(_translate("MainWindow", "...", None))
        self.facesStatsNumber.setText(_translate("MainWindow", "Nalezené obličeje/Celkový počet souborů:", None))

