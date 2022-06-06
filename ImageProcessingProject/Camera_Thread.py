import cv2
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CameraThread(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):
        self.isThreadActive = True

        cap = cv2.VideoCapture(0)

        while self.isThreadActive:
            ret, self.frame = cap.read()

            if ret:
                rgbImage = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(
                    rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                self.changePixmap.emit(convertToQtFormat)

        cap.release()

    def closeCamera(self):
        self.isThreadActive = False
        self.quit()

    def snapCamera(self):
        if self.isThreadActive:
            cv2.imwrite("snapped-image.png", self.frame)
