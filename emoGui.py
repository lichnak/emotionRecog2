from PyQt4 import QtCore, QtGui, uic
import cv2
import numpy
import sys
import glob
from datetime import datetime
from gui3 import Ui_MainWindow
import os
import errno
import copy
import ctypes
import numpy as np


def get_files(emotion):
    global emotion_db, to_classify_dir
    files = glob.glob(str(emotion_db) + "\\%s\\*" % emotion)
    files2 = glob.glob(str(to_classify_dir) + "\*.jpg")

    training = files[:int(len(files) * 0.1)]  # get first 80% of file list
    # prediction = files[-int(len(files) * 0.5):]  # get last 20% of file list
    prediction = files2
    return training, prediction


def make_sets():
    training_data = []
    training_labels = []
    prediction_data = []
    prediction_labels = []
    for emotion in emotions:
        training, prediction = get_files(emotion)

        # Append data to training and prediction list, and generate labels 0-7
        for item in training:
            image = cv2.imread(item)  # open image
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert to grayscale
            training_data.append(gray)  # append image array to training data list
            training_labels.append(emotions.index(emotion))

    for item in prediction:  # repeat above process for prediction set
        image = cv2.imread(item)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        prediction_data.append(gray)
        prediction_labels.append(item)

    return training_data, training_labels, prediction_data, prediction_labels


def run_recognizer():
    global to_classify_dir
    cnt_neutral = 0
    cnt_anger = 0
    cnt_contempt = 0
    cnt_disgust = 0
    cnt_happy = 0
    cnt_sadness = 0
    cnt_surprise = 0

    training_data, training_labels, prediction_data, prediction_labels = make_sets()
    myapp.ui.textLog.append("training fisher face classifier")
    myapp.ui.textLog.append("size of training set is: " + str(len(training_labels)) + " images")
    fishface.train(training_data, np.asarray(training_labels))
    myapp.ui.textLog.append("predicting classification set")
    cnt = 0
    for image in prediction_data:

        pred, conf = fishface.predict(image)
        myapp.ui.textLog.append('Emoce: %s' % prediction_labels[cnt] + " " + str(emotions[pred]))
        os.rename(prediction_labels[cnt], to_classify_dir + "/" + prediction_labels[cnt][-27:-4] + "_"
                  + emotions[pred] + ".jpg")
        if emotions[pred] == "neutral":
            cnt_neutral += 1
        elif emotions[pred] == "anger":
            cnt_anger += 1
        elif emotions[pred] == "contempt":
            cnt_contempt += 1
        elif emotions[pred] == "disgust":
            cnt_disgust += 1
        elif emotions[pred] == "happy":
            cnt_happy += 1
        elif emotions[pred] == "sadness":
            cnt_sadness += 1
        elif emotions[pred] == "surprise":
            cnt_surprise += 1

        cnt += 1
        #if pred == prediction_labels[cnt]:
        #    correct += 1
        #    cnt += 1
        #else:
        #    incorrect += 1
        #    cnt += 1
    f = open(to_classify_dir + '/summary.txt', 'w')
    text = "neutral: %s" % cnt_neutral + " (%s" + str(float(cnt_neutral) / cnt) + "%)" + "\n" \
        "anger: %s" % cnt_anger + " (" + str(float(cnt_anger) / cnt) + "%)" + "\n" \
        "contempt: %s" % cnt_contempt + " (" + str(float(cnt_contempt) / cnt) + "%)" + "\n" \
        "disgust: %s" % cnt_disgust + " (" + str(float(cnt_disgust) / cnt) + "%)" + "\n" \
        "happy: %s" % cnt_happy + " (" + str(float(cnt_happy) / cnt) + "%)" + "\n" \
        "sadness: %s" % cnt_sadness + " (" + str(float(cnt_sadness) / cnt) + "%)" + "\n" \
        "surprise: %s" % cnt_surprise + " (" + str(float(cnt_surprise) / cnt) + "%)" + "\n"
    f.write(text)
    f.write("Celkovy pocet snimku s detekovanym oblicejem: " + str(cnt))
    MessageBox = ctypes.windll.user32.MessageBoxA
    MessageBox(0, 'Vysledky klasifikace viz summary.txt', 'Hotovo', 0x0)
    return 0

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyForm, self).__init__()

        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Emotion Recognition Python Tool')
        self.ui.startButton.clicked.connect(self.start_clicked)
        self.ui.stopButton.clicked.connect(self.stop_clicked)
        self.ui.selectSaveDirButton.clicked.connect(self.select_save_clicked)
        self.ui.selectProcessDirButton.clicked.connect(self.select_process_clicked)
        self.ui.preprocessButton.clicked.connect(self.face_detection)
        self.ui.classificationButton.clicked.connect(self.emotion_detection)
        self.ui.saveNoteButton.clicked.connect(self.save_note)
        self.ui.cameraButton.clicked.connect(self.camera_enabler)
        self.ui.cameraDisableButton.clicked.connect(self.camera_disabler)
        self.ui.selectEmotionDbButton.clicked.connect(self.emotion_db_path)
        self.ui.selectClassificationDirButton.clicked.connect(self.select_classification_dir)

        self.ui.textLog.append("Start...")

        timer1 = QtCore.QTimer(self)
        timer1.timeout.connect(self.open)
        timer1.start(101)  # 10 Hz

        timer2 = QtCore.QTimer(self)
        timer2.timeout.connect(self.save)
        timer2.start(333)  # 3 za sekundu

    def open(self):
        # get data and display
        global cap, frame_pure, faceCascade, image_enabled
        if image_enabled:
            ret, frame_pure = cap.read()
            frame = copy.deepcopy(frame_pure)
            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.05,
                minNeighbors=8,
                minSize=(55, 55),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            for (x, y, w, h) in faces:

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            height, width, channel = frame.shape
            bytesperline = 3 * width
            qimg = QtGui.QImage(frame, width, height, bytesperline, QtGui.QImage.Format_RGB888)
            image = QtGui.QPixmap.fromImage(qimg)
            if image.isNull():
                QtGui.QMessageBox.information(self, "Image Viewer","Cannot load")
                return
            lbl = QtGui.QLabel(self.ui.graphicsView)
            lbl.setPixmap(image)
            lbl.show()

    def save(self):
        global frame_pure, count, running, save_path
        if running:
            count += 1
            gray = cv2.cvtColor(frame_pure, cv2.COLOR_BGR2GRAY)
            # Display the resulting frame
            # cv2.imshow('frame', gray)
            frameTime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')[:-3]
            self.ui.textLog.append(unicode("Ukladam obrazek: " + save_path) + '/' + frameTime + '.jpg')
            cesta = unicode((unicode(save_path) + '/' + frameTime + '.jpg'))
            cv2.imwrite(cesta, gray)
            self.ui.savedPicsNumber.setText('Ulozeno obrazku: ' + str(count))

    def start_clicked(self):
        global running, save_directory, save_path
        new_folder_name = unicode(self.ui.textEditExperiment.toPlainText())
        try:
            os.makedirs(str(save_directory) + '/' + new_folder_name)
            save_path = str(save_directory) + '/' + new_folder_name
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
            elif exception.errno == errno.EEXIST:
                save_path = str(save_directory) + '/' + new_folder_name
        running = True
        self.ui.startButton.setEnabled(False)
        self.ui.textEditExperiment.setEnabled(False)
        self.ui.startButton.setText('Ukladam...')
        self.ui.stopButton.setEnabled(True)

    def stop_clicked(self):
        global running
        running = False
        self.ui.startButton.setEnabled(True)
        self.ui.startButton.setText('Start')
        self.ui.stopButton.setEnabled(False)
        self.ui.textEditExperiment.setEnabled(True)

    def select_save_clicked(self):
        global save_directory
        save_directory = QtGui.QFileDialog.getExistingDirectory(self, "Vyberte adresar pro ukladani obrazku")
        self.ui.textSavePath.setText(save_directory)

    def select_process_clicked(self):
        global process_directory
        process_directory = QtGui.QFileDialog.getExistingDirectory(self, "Vyberte adresar pro zpracovani obrazku")
        files = glob.glob(str(process_directory) + "\*.jpg")
        self.ui.facesStatsNumber.setText("Nalezene obliceje/Celkovy pocet souboru: 0/" + str(len(files)))
        self.ui.preprocessButton.setEnabled(True)
        self.ui.textProcessPath.setText(process_directory)

    def face_detection(self):
        global process_directory, save_path
        self.ui.preprocessButton.setEnabled(False)
        faces_found = 0
        try:
            processed_path = str(process_directory) + '/processed'
            os.makedirs(str(process_directory) + '/processed')
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

        faceDet = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        faceDet2 = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
        faceDet3 = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
        faceDet4 = cv2.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")
        files = glob.glob(str(process_directory) + "\*.jpg")

        filenumber = 0
        for f in files:
            face_image = cv2.imread(f)  # Open image
            f_name = "proc" + f[-27:]
            gray = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)  # Convert image to grayscale

            # Detect face using 4 different classifiers
            face = faceDet.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5),
                                            flags=cv2.CASCADE_SCALE_IMAGE)
            face2 = faceDet2.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5),
                                              flags=cv2.CASCADE_SCALE_IMAGE)
            face3 = faceDet3.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5),
                                              flags=cv2.CASCADE_SCALE_IMAGE)
            face4 = faceDet4.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5),
                                              flags=cv2.CASCADE_SCALE_IMAGE)

            # Go over detected faces, stop at first detected face, return empty if no face.
            if len(face) == 1:
                facefeatures = face
            elif len(face2) == 1:
                facefeatures = face2
            elif len(face3) == 1:
                facefeatures = face3
            elif len(face4) == 1:
                facefeatures = face4
            else:
                facefeatures = ""

            # Cut and save face
            for (x, y, w, h) in facefeatures:  # get coordinates and size of rectangle containing face
                myapp.ui.textLog.append("face found in file: %s" % f)
                faces_found += 1
                gray = gray[y:y + h + 10, x:x + w + 10]  # Cut the frame to size
                self.ui.facesStatsNumber.setText("Nalezene obliceje/Celkovy pocet souboru: " + str(faces_found) + "/"
                                                 + str(len(files)))
                try:
                    out = cv2.resize(gray, (350, 350))  # Resize face so all images have same size
                    cv2.imwrite(str(processed_path) + '/' + f_name, out)  # Write image
                except:
                    pass  # If error, pass file
            filenumber += 1  # Increment image number
        self.ui.preprocessButton.setEnabled(True)

    def emotion_detection(self):
        run_recognizer()

    def save_note(self):
        global running, save_directory, save_path
        new_folder_name = unicode(self.ui.textEditExperiment.toPlainText())
        try:
            os.makedirs(str(save_directory) + '/' + new_folder_name)
            save_path = str(save_directory) + '/' + new_folder_name
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
            elif exception.errno == errno.EEXIST:
                save_path = str(save_directory) + '/' + new_folder_name
        f = open(save_path + '/poznamka.txt', 'w')
        text = self.ui.textEditNote.toPlainText()
        f.write(text)
        self.ui.textLog.append("Poznamka ulozena do " + str(save_path + '/poznamka.txt'))

    def camera_enabler(self):
        global image_enabled, cap, camera_slot
        camera_found = False
        camera_accepted = False
        camera_slot = 0
        if not image_enabled:
            while camera_slot < 10 and not camera_accepted:
                self.ui.textLog.append("Hledam kameru ve slotu " + str(camera_slot))
                if cv2.VideoCapture(camera_slot).isOpened():
                    self.ui.textLog.append("Kamera nalezena")
                    MessageBox = ctypes.windll.user32.MessageBoxA
                    result = MessageBox(0, 'Pouzit kameru ve slotu ' + str(int(camera_slot)) + '?', 'Kamera nalezena', 0x04)
                    if result == 6:
                        camera_accepted = True
                        self.ui.textLog.append("Pouzivam kameru ve slotu: " + str(camera_slot))
                        self.ui.startButton.setEnabled(True)
                    else:
                        camera_accepted = False
                        camera_slot += 1
                else:
                    camera_slot += 1


            if camera_accepted:
                image_enabled = not image_enabled
                if image_enabled:
                    self.ui.cameraButton.setEnabled(False)
                    cap = cv2.VideoCapture(camera_slot)
                else:
                    cap.release()
                    self.ui.cameraButton.setEnabled(True)

    def camera_disabler(self):
        global cap, image_enabled
        image_enabled = False
        cap.release()
        self.ui.cameraButton.setEnabled(True)
        self.ui.startButton.setEnabled(False)
        self.ui.textLog.append("Kamera vypnuta")

    def emotion_db_path(self):
        global emotion_db
        emotion_db = QtGui.QFileDialog.getExistingDirectory(self, "Vyberte adresar obsahujici databazi emoci")
        self.ui.textEmotionDb.setText(emotion_db)

    def select_classification_dir(self):
        global to_classify_dir
        to_classify_dir = QtGui.QFileDialog.getExistingDirectory(self, "Vyberte adresar obsahujici obrazky ke klasifikaci")
        self.ui.textClassificationPath.setText(to_classify_dir)
        self.ui.classificationButton.setEnabled(True)


if __name__ == '__main__':
    global save_directory, save_path, frame_pure, image_enabled
    #emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]  # Emotion list
    # emotions = ["neutral", "anger", "disgust", "happy"]
    emotions = ["neutral", "anger", "contempt", "disgust", "happy", "sadness", "surprise"]

    fishface = cv2.createFisherFaceRecognizer()  # Initialize fisher face classifier
    data = {}

    image_enabled = False
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # faceCascade = cv2.CascadeClassifier("lbpcascade_frontalface.xml")
    #cap = cv2.VideoCapture(0)
    #ret0, frame_pure = cap.read()
    count = 0
    save_directory = os.path.abspath('E:/Emotions')
    save_path = save_directory
    running = False
    form_class = uic.loadUiType("gui3.ui")[0]
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


