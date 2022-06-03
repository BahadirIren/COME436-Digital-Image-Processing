import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Ui_Main_Window as pyUi
import Camera_Thread as cThread


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = pyUi.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        # -------------- Connect Section --------------
        self.ui.openButton.clicked.connect(self.openCamera)
        self.ui.closeButton.clicked.connect(self.closeCamera)
        self.ui.snapButton.clicked.connect(self.snapCamera)

        # -------------- Image Processing Section --------------
        self.ui.loadImageButton.clicked.connect(self.loadImage)

        # -------------- Extra Section --------------
        self.ui.exitButton.clicked.connect(self.exit)

    # -------------- Connect Section --------------
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.ui.imageLabel.setPixmap(QPixmap.fromImage(image))

    def openCamera(self):
        self.thread = cThread.CameraThread(self)
        self.thread.changePixmap.connect(self.setImage)
        self.thread.start()

        self.ui.snapButton.setEnabled(True)
        self.ui.openButton.setEnabled(False)
        self.ui.closeButton.setEnabled(True)
        self.setImageProcessingButtonsEnabled(False)

    def closeCamera(self):
        self.thread.closeCamera()

        self.ui.snapButton.setEnabled(False)
        self.ui.openButton.setEnabled(True)
        self.ui.closeButton.setEnabled(False)

    def snapCamera(self):
        self.thread.snapCamera()

    # -------------- Image Processing Section --------------
    def loadImage(self):
        if isinstance(self.thread, cThread.CameraThread):
            self.closeCamera()

        fileName, _ = QFileDialog.getOpenFileName(self, 'Open file', '',
                                                        "Image files (*.jpg *.png *.jpeg)")
        if fileName:
            self.ui.imageLabel.setPixmap(QPixmap(fileName))

            self.ui.snapButton.setEnabled(False)
            self.ui.openButton.setEnabled(True)
            self.ui.closeButton.setEnabled(False)
            self.setImageProcessingButtonsEnabled(True)

    def setImageProcessingButtonsEnabled(self, isEnabled):
        self.ui.cropAndSaveButton.setEnabled(isEnabled)
        self.ui.convertToGrayButton.setEnabled(isEnabled)
        self.ui.convertToBlackAndWhiteButton.setEnabled(isEnabled)
        self.ui.take2DFastFourierTransformButton.setEnabled(isEnabled)
        self.ui.addGaussianNoiseButton.setEnabled(isEnabled)
        self.ui.addPepperAndSaltNoiseButton.setEnabled(isEnabled)
        self.ui.meanFilterButton.setEnabled(isEnabled)
        self.ui.medianFilterButton.setEnabled(isEnabled)
        self.ui.gaussianFilterButton.setEnabled(isEnabled)
        self.ui.edgesButton.setEnabled(isEnabled)
        self.ui.cornersButton.setEnabled(isEnabled)

    # -------------- Extra Section --------------
    def exit(self):
        self.closeCamera()
        sys.exit()
