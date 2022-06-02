import cv2
import sys
from PyQt5.uic import loadUi
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("Digital-Image-Project.ui", self)

        self.loadImageButton.clicked.connect(self.addImage)

        self.openButton.clicked.connect(self.openCamera)
        self.closeButton.clicked.connect(self.closeCamera)
        self.snapButton.clicked.connect(self.snapCamera)

        self.exitButton.clicked.connect(self.exit)

    def addImage(self):
        qPixMap = QPixmap("python-logo.png")
        self.imageLabel.setPixmap(qPixMap)

    def snapCamera(self):
        self.thread.snapCamera()

    def closeCamera(self):
        self.thread.closeCamera()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.imageLabel.setPixmap(QPixmap.fromImage(image))

    def openCamera(self):
        # TODO kamera acikken tekrar acmaya basarsa kapatma calismiyor
        self.thread = Thread(self)
        self.thread.changePixmap.connect(self.setImage)
        self.thread.start()

    def exit(self):
        self.closeCamera()
        sys.exit()


class Thread(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):
        self.threadActive = True

        cap = cv2.VideoCapture(0)

        while self.threadActive:
            ret, self.frame = cap.read()

            if ret:
                rgbImage = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(
                    rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

        cap.release()

    def closeCamera(self):
        if self.isRunning:
            self.threadActive = False
            self.quit()

    def snapCamera(self):
        if self.threadActive:
            cv2.imwrite("snapped-image.png", self.frame)


# main
app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
