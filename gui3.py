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
        MainWindow.resize(1180, 891)
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
        self.stopButton.setEnabled(False)
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
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(650, 50, 20, 341))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1130, 50, 20, 341))
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
        self.line_5.setGeometry(QtCore.QRect(650, 400, 20, 401))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(660, 390, 481, 16))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(1130, 400, 20, 401))
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.zpracovaniLabel = QtGui.QLabel(self.centralwidget)
        self.zpracovaniLabel.setGeometry(QtCore.QRect(670, 400, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zpracovaniLabel.setFont(font)
        self.zpracovaniLabel.setObjectName(_fromUtf8("zpracovaniLabel"))
        self.textProcessPath = QtGui.QTextEdit(self.centralwidget)
        self.textProcessPath.setEnabled(False)
        self.textProcessPath.setGeometry(QtCore.QRect(680, 430, 421, 31))
        self.textProcessPath.setObjectName(_fromUtf8("textProcessPath"))
        self.selectProcessDirButton = QtGui.QPushButton(self.centralwidget)
        self.selectProcessDirButton.setGeometry(QtCore.QRect(1110, 430, 21, 28))
        self.selectProcessDirButton.setObjectName(_fromUtf8("selectProcessDirButton"))
        self.preprocessButton = QtGui.QPushButton(self.centralwidget)
        self.preprocessButton.setEnabled(False)
        self.preprocessButton.setGeometry(QtCore.QRect(680, 470, 131, 28))
        self.preprocessButton.setObjectName(_fromUtf8("preprocessButton"))
        self.classificationButton = QtGui.QPushButton(self.centralwidget)
        self.classificationButton.setEnabled(False)
        self.classificationButton.setGeometry(QtCore.QRect(680, 640, 131, 28))
        self.classificationButton.setObjectName(_fromUtf8("classificationButton"))
        self.textEditNote = QtGui.QTextEdit(self.centralwidget)
        self.textEditNote.setGeometry(QtCore.QRect(680, 190, 451, 141))
        self.textEditNote.setObjectName(_fromUtf8("textEditNote"))
        self.ukladaniLabel_2 = QtGui.QLabel(self.centralwidget)
        self.ukladaniLabel_2.setGeometry(QtCore.QRect(670, 160, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ukladaniLabel_2.setFont(font)
        self.ukladaniLabel_2.setObjectName(_fromUtf8("ukladaniLabel_2"))
        self.saveNoteButton = QtGui.QPushButton(self.centralwidget)
        self.saveNoteButton.setEnabled(True)
        self.saveNoteButton.setGeometry(QtCore.QRect(1020, 340, 111, 31))
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
        self.textClassificationPath.setGeometry(QtCore.QRect(670, 540, 421, 31))
        self.textClassificationPath.setObjectName(_fromUtf8("textClassificationPath"))
        self.selectClassificationDirButton = QtGui.QPushButton(self.centralwidget)
        self.selectClassificationDirButton.setGeometry(QtCore.QRect(1100, 540, 21, 28))
        self.selectClassificationDirButton.setObjectName(_fromUtf8("selectClassificationDirButton"))
        self.facesStatsNumber = QtGui.QLabel(self.centralwidget)
        self.facesStatsNumber.setGeometry(QtCore.QRect(820, 470, 311, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.facesStatsNumber.setFont(font)
        self.facesStatsNumber.setObjectName(_fromUtf8("facesStatsNumber"))
        self.textEmotionDb = QtGui.QTextEdit(self.centralwidget)
        self.textEmotionDb.setEnabled(False)
        self.textEmotionDb.setGeometry(QtCore.QRect(670, 600, 421, 31))
        self.textEmotionDb.setObjectName(_fromUtf8("textEmotionDb"))
        self.dbEmotionLabel = QtGui.QLabel(self.centralwidget)
        self.dbEmotionLabel.setGeometry(QtCore.QRect(670, 570, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dbEmotionLabel.setFont(font)
        self.dbEmotionLabel.setObjectName(_fromUtf8("dbEmotionLabel"))
        self.line_12 = QtGui.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(660, 500, 481, 16))
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.selectEmotionDbButton = QtGui.QPushButton(self.centralwidget)
        self.selectEmotionDbButton.setGeometry(QtCore.QRect(1100, 600, 21, 28))
        self.selectEmotionDbButton.setObjectName(_fromUtf8("selectEmotionDbButton"))
        self.dbEmotionLabel_2 = QtGui.QLabel(self.centralwidget)
        self.dbEmotionLabel_2.setGeometry(QtCore.QRect(670, 510, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dbEmotionLabel_2.setFont(font)
        self.dbEmotionLabel_2.setObjectName(_fromUtf8("dbEmotionLabel_2"))
        self.line_13 = QtGui.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(660, 670, 481, 16))
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(660, 380, 481, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.textLog = QtGui.QTextEdit(self.centralwidget)
        self.textLog.setEnabled(True)
        self.textLog.setGeometry(QtCore.QRect(10, 580, 631, 211))
        self.textLog.setReadOnly(True)
        self.textLog.setObjectName(_fromUtf8("textLog"))
        self.textVideoPath = QtGui.QTextEdit(self.centralwidget)
        self.textVideoPath.setEnabled(False)
        self.textVideoPath.setGeometry(QtCore.QRect(670, 720, 421, 31))
        self.textVideoPath.setObjectName(_fromUtf8("textVideoPath"))
        self.selectVideoDirButton = QtGui.QPushButton(self.centralwidget)
        self.selectVideoDirButton.setGeometry(QtCore.QRect(1100, 720, 21, 28))
        self.selectVideoDirButton.setObjectName(_fromUtf8("selectVideoDirButton"))
        self.line_10 = QtGui.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(660, 790, 481, 16))
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.videoButton = QtGui.QPushButton(self.centralwidget)
        self.videoButton.setEnabled(False)
        self.videoButton.setGeometry(QtCore.QRect(670, 760, 131, 28))
        self.videoButton.setObjectName(_fromUtf8("videoButton"))
        self.dbEmotionLabel_3 = QtGui.QLabel(self.centralwidget)
        self.dbEmotionLabel_3.setGeometry(QtCore.QRect(670, 680, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dbEmotionLabel_3.setFont(font)
        self.dbEmotionLabel_3.setObjectName(_fromUtf8("dbEmotionLabel_3"))
        self.dbEmotionLabel_4 = QtGui.QLabel(self.centralwidget)
        self.dbEmotionLabel_4.setGeometry(QtCore.QRect(10, 540, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dbEmotionLabel_4.setFont(font)
        self.dbEmotionLabel_4.setObjectName(_fromUtf8("dbEmotionLabel_4"))
        self.trainRButton = QtGui.QRadioButton(self.centralwidget)
        self.trainRButton.setGeometry(QtCore.QRect(820, 640, 141, 17))
        self.trainRButton.setObjectName(_fromUtf8("trainRButton"))
        self.pretrainRButton = QtGui.QRadioButton(self.centralwidget)
        self.pretrainRButton.setGeometry(QtCore.QRect(820, 660, 151, 17))
        self.pretrainRButton.setChecked(True)
        self.pretrainRButton.setObjectName(_fromUtf8("pretrainRButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1180, 21))
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
        self.textEmotionDb.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.dbEmotionLabel.setText(_translate("MainWindow", "Cesta k databázi emocí", None))
        self.selectEmotionDbButton.setText(_translate("MainWindow", "...", None))
        self.dbEmotionLabel_2.setText(_translate("MainWindow", "Složka obsahující soubory s nalezenými obličeji", None))
        self.textVideoPath.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.selectVideoDirButton.setText(_translate("MainWindow", "...", None))
        self.videoButton.setText(_translate("MainWindow", "Zkonvertovat video", None))
        self.dbEmotionLabel_3.setText(_translate("MainWindow", "Konverze videa", None))
        self.dbEmotionLabel_4.setText(_translate("MainWindow", "Log", None))
        self.trainRButton.setText(_translate("MainWindow", "Použit zvolenou db", None))
        self.pretrainRButton.setText(_translate("MainWindow", "Předtrénovaný klasifikátor", None))

