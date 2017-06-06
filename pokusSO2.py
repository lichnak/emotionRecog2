from PyQt4 import QtCore, QtGui, uic
import cv2
import numpy
from test1gui import Ui_MainWindow

class MyForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MyForm, self).__init__()

        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('GUI')
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.open)
        timer.start(101) #30 Hz

        timer2 = QtCore.QTimer(self)
        timer2.timeout.connect(self.save)
        timer2.start(1000) #1 za sekundu

    def open(self):
        #get data and display
        global cap, frame, faceCascade
        sF = 1.05
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=sF,
            minNeighbors=8,
            minSize=(55, 55),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        for (x, y, w, h) in faces:

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        height, width, channel = frame.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(frame, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        image = QtGui.QPixmap.fromImage(qImg)
        if image.isNull():
            QtGui.QMessageBox.information(self, "Image Viewer","Cannot load ")
            return

        lbl = QtGui.QLabel(self.ui.graphicsView)
        lbl.setPixmap(image)
        lbl.show()

        #self.ui.QLabel.setPixmap(image)
        #self.ui.QLabel.adjustSize()


    def save(self):
        global frame, count
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        # cv2.imshow('frame', gray)
        cv2.imwrite('./webcam_pics/' + str(count) + '.jpg', gray)
        count += 1


class CameraViewer(QtGui.QMainWindow):
    def __init__(self):
        super(CameraViewer, self).__init__()

        self.imageLabel = QtGui.QLabel()
        self.imageLabel.setBackgroundRole(QtGui.QPalette.Base)
        self.imageLabel.setScaledContents(True)

        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setWidget(self.imageLabel)
        self.setCentralWidget(self.scrollArea)

        self.setWindowTitle("Image Viewer")
        self.resize(640, 480)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.open)
        timer.start(101) #30 Hz

        timer2 = QtCore.QTimer(self)
        timer2.timeout.connect(self.save)
        timer2.start(1000) #1 za sekundu

    def open(self):
        #get data and display
        global cap, frame, faceCascade
        sF = 1.05
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=sF,
            minNeighbors=8,
            minSize=(55, 55),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        for (x, y, w, h) in faces:

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        height, width, channel = frame.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(frame, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        image = QtGui.QPixmap.fromImage(qImg)
        if image.isNull():
            QtGui.QMessageBox.information(self, "Image Viewer","Cannot load ")
            return

        self.imageLabel.setPixmap(image)
        self.imageLabel.adjustSize()


    def save(self):
        global frame, count
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        # cv2.imshow('frame', gray)
        cv2.imwrite('./webcam_pics/' + str(count) + '.jpg', gray)
        count += 1

if __name__ == '__main__':

    import sys

    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    #faceCascade = cv2.CascadeClassifier("lbpcascade_frontalface.xml")

    cap = cv2.VideoCapture(1)
    ret, frame = cap.read()
    count = 0

    form_class = uic.loadUiType("gui1.ui")[0]
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()

    # app = QtGui.QApplication(sys.argv)
    # CameraViewer = CameraViewer()
    # CameraViewer.show()
    sys.exit(app.exec_())

