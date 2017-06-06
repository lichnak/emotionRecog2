# -*- coding: utf-8 -*-
# pred zacatkem pyuic4 untitled.ui -o test1gui.py
from PyQt4 import QtCore, QtGui, uic
import sys
import cv2
import numpy as np
import threading
import time
import Queue
from test1gui import Ui_MainWindow


__author__ = "Jan Vrba"
__copyright__ = "Copyright 2016, kurokesu.com"
__version__ = "0.1"
__license__ = "GPL"
running = False
capture_thread = None
form_class = uic.loadUiType("gui1.ui")[0]
q = Queue.Queue()
cap = cv2.VideoCapture(1)
count = 0


def grab():
    global running, count, cap
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        #cv2.imshow('frame', gray)
        cv2.imwrite('./webcam_pics/' + str(count) + '.jpg', gray)
        count += 1
        time.sleep(1)

class MyForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('GUI')

        self.ui.startButton.clicked.connect(self.start_clicked)
        self.ui.stopButton.clicked.connect(self.stop_clicked)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(2)

    def start_clicked(self):
        global running
        running = True
        capture_thread.start()
        self.ui.startButton.setEnabled(False)
        self.ui.startButton.setText('Starting...')

    def stop_clicked(self):
        global running
        running = False

    def update_frame(self):
        self.ui.textEdit.setText('Chci delat obrazky')
        pixmap = QtGui.QPixmap('./webcam_pics/' + str(count) + '.jpg')
        lbl = QtGui.QLabel(self.ui.graphicsView)
        lbl.setPixmap(pixmap)
        lbl.show()


capture_thread = threading.Thread(target=grab)
app = QtGui.QApplication(sys.argv)
myapp = MyForm()
myapp.show()
sys.exit(app.exec_())