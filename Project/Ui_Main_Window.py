from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 823)
        MainWindow.setMinimumSize(QtCore.QSize(543, 600))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 555))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(270, 0))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("QScrollArea {\n"
                                      "    border: none;\n"
                                      "}")
        self.scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 255, 824))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.sideMenu = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sideMenu.sizePolicy().hasHeightForWidth())
        self.sideMenu.setSizePolicy(sizePolicy)
        self.sideMenu.setMinimumSize(QtCore.QSize(0, 800))
        self.sideMenu.setTabletTracking(False)
        self.sideMenu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sideMenu.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.sideMenu.setAcceptDrops(False)
        self.sideMenu.setAutoFillBackground(False)
        self.sideMenu.setStyleSheet("QFrame {\n"
                                    "    border: none;\n"
                                    "}")
        self.sideMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sideMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sideMenu.setObjectName("sideMenu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sideMenu)
        self.verticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.connectLabel = QtWidgets.QLabel(self.sideMenu)
        self.connectLabel.setStyleSheet("background-color: red;\n"
                                        "color: white;\n"
                                        "font-size: 18px;\n"
                                        "padding: 5px;")
        self.connectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.connectLabel.setObjectName("connectLabel")
        self.verticalLayout.addWidget(self.connectLabel)
        self.openButton = QtWidgets.QToolButton(self.sideMenu)
        self.openButton.setMouseTracking(False)
        self.openButton.setAcceptDrops(False)
        self.openButton.setAutoFillBackground(False)
        self.openButton.setStyleSheet("QToolButton{\n"
                                      "    background-color: white;\n"
                                      "    color: black;\n"
                                      "    font-size: 12px;\n"
                                      "    width: 220%;\n"
                                      "    height: 15%;\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:hover{\n"
                                      "    background-color:  blue;\n"
                                      "    color: white;\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:pressed{\n"
                                      "    background-color:  white;\n"
                                      "    color: black;\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:disabled{\n"
                                      "    background-color:  gray;\n"
                                      "    color: white;\n"
                                      "}")
        self.openButton.setCheckable(False)
        self.openButton.setChecked(False)
        self.openButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.openButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.openButton.setAutoRaise(False)
        self.openButton.setArrowType(QtCore.Qt.NoArrow)
        self.openButton.setObjectName("openButton")
        self.verticalLayout.addWidget(self.openButton)
        self.closeButton = QtWidgets.QToolButton(self.sideMenu)
        self.closeButton.setEnabled(False)
        self.closeButton.setAcceptDrops(False)
        self.closeButton.setStyleSheet("QToolButton{\n"
                                       "    background-color: white;\n"
                                       "    color: black;\n"
                                       "    font-size: 12px;\n"
                                       "    width: 220%;\n"
                                       "    height: 15%;\n"
                                       "}\n"
                                       "\n"
                                       "QToolButton:hover{\n"
                                       "    background-color:  blue;\n"
                                       "    color: white;\n"
                                       "}\n"
                                       "\n"
                                       "QToolButton:pressed{\n"
                                       "    background-color:  white;\n"
                                       "    color: black;\n"
                                       "}\n"
                                       "\n"
                                       "QToolButton:disabled{\n"
                                       "    background-color:  gray;\n"
                                       "    color: white;\n"
                                       "}")
        self.closeButton.setCheckable(False)
        self.closeButton.setChecked(False)
        self.closeButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.closeButton.setAutoRaise(False)
        self.closeButton.setArrowType(QtCore.Qt.NoArrow)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)
        self.snapButton = QtWidgets.QToolButton(self.sideMenu)
        self.snapButton.setEnabled(False)
        self.snapButton.setStyleSheet("QToolButton{\n"
                                      "    background-color: white;\n"
                                      "    color: black;\n"
                                      "    font-size: 12px;\n"
                                      "    width: 220%;\n"
                                      "    height: 15%;\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:hover{\n"
                                      "    background-color:  blue;\n"
                                      "    color: white;\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:pressed{\n"
                                      "    background-color:  white;\n"
                                      "    color: black;\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:disabled{\n"
                                      "    background-color:  gray;\n"
                                      "    color: white;\n"
                                      "}")
        self.snapButton.setCheckable(False)
        self.snapButton.setObjectName("snapButton")
        self.verticalLayout.addWidget(self.snapButton)
        self.imageProcessingLabel = QtWidgets.QLabel(self.sideMenu)
        self.imageProcessingLabel.setStyleSheet("background-color: red;\n"
                                                "color: white;\n"
                                                "font-size: 18px;\n"
                                                "padding: 5px;")
        self.imageProcessingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageProcessingLabel.setObjectName("imageProcessingLabel")
        self.verticalLayout.addWidget(self.imageProcessingLabel)
        self.loadImageButton = QtWidgets.QToolButton(self.sideMenu)
        self.loadImageButton.setStyleSheet("QToolButton{\n"
                                           "    background-color: white;\n"
                                           "    color: black;\n"
                                           "    font-size: 12px;\n"
                                           "    width: 220%;\n"
                                           "    height: 15%;\n"
                                           "}\n"
                                           "\n"
                                           "QToolButton:hover{\n"
                                           "    background-color:  blue;\n"
                                           "    color: white;\n"
                                           "}\n"
                                           "\n"
                                           "QToolButton:pressed{\n"
                                           "    background-color:  white;\n"
                                           "    color: black;\n"
                                           "}\n"
                                           "\n"
                                           "QToolButton:disabled{\n"
                                           "    background-color:  gray;\n"
                                           "    color: white;\n"
                                           "}")
        self.loadImageButton.setCheckable(False)
        self.loadImageButton.setObjectName("loadImageButton")
        self.verticalLayout.addWidget(self.loadImageButton)
        self.cropAndSaveButton = QtWidgets.QToolButton(self.sideMenu)
        self.cropAndSaveButton.setEnabled(False)
        self.cropAndSaveButton.setStyleSheet("QToolButton{\n"
                                             "    background-color: white;\n"
                                             "    color: black;\n"
                                             "    font-size: 12px;\n"
                                             "    width: 220%;\n"
                                             "    height: 15%;\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton:hover{\n"
                                             "    background-color:  blue;\n"
                                             "    color: white;\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton:pressed{\n"
                                             "    background-color:  white;\n"
                                             "    color: black;\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton:disabled{\n"
                                             "    background-color:  gray;\n"
                                             "    color: white;\n"
                                             "}")
        self.cropAndSaveButton.setCheckable(False)
        self.cropAndSaveButton.setObjectName("cropAndSaveButton")
        self.verticalLayout.addWidget(self.cropAndSaveButton)
        self.imageAnalysisGroupBox = QtWidgets.QGroupBox(self.sideMenu)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.imageAnalysisGroupBox.sizePolicy().hasHeightForWidth())
        self.imageAnalysisGroupBox.setSizePolicy(sizePolicy)
        self.imageAnalysisGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.imageAnalysisGroupBox.setStyleSheet("")
        self.imageAnalysisGroupBox.setObjectName("imageAnalysisGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.imageAnalysisGroupBox)
        self.verticalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.convertToGrayButton = QtWidgets.QToolButton(
            self.imageAnalysisGroupBox)
        self.convertToGrayButton.setEnabled(False)
        self.convertToGrayButton.setStyleSheet("QToolButton{\n"
                                               "    background-color: white;\n"
                                               "    color: black;\n"
                                               "    font-size: 12px;\n"
                                               "    width: 220%;\n"
                                               "    height: 15%;\n"
                                               "}\n"
                                               "\n"
                                               "QToolButton:hover{\n"
                                               "    background-color:  blue;\n"
                                               "    color: white;\n"
                                               "}\n"
                                               "\n"
                                               "QToolButton:pressed{\n"
                                               "    background-color:  white;\n"
                                               "    color: black;\n"
                                               "}\n"
                                               "\n"
                                               "QToolButton:disabled{\n"
                                               "    background-color:  gray;\n"
                                               "    color: white;\n"
                                               "}")
        self.convertToGrayButton.setCheckable(False)
        self.convertToGrayButton.setObjectName("convertToGrayButton")
        self.verticalLayout_2.addWidget(self.convertToGrayButton)
        self.convertToBlackAndWhiteButton = QtWidgets.QToolButton(
            self.imageAnalysisGroupBox)
        self.convertToBlackAndWhiteButton.setEnabled(False)
        self.convertToBlackAndWhiteButton.setStyleSheet("QToolButton{\n"
                                                        "    background-color: white;\n"
                                                        "    color: black;\n"
                                                        "    font-size: 12px;\n"
                                                        "    width: 220%;\n"
                                                        "    height: 15%;\n"
                                                        "}\n"
                                                        "\n"
                                                        "QToolButton:hover{\n"
                                                        "    background-color:  blue;\n"
                                                        "    color: white;\n"
                                                        "}\n"
                                                        "\n"
                                                        "QToolButton:pressed{\n"
                                                        "    background-color:  white;\n"
                                                        "    color: black;\n"
                                                        "}\n"
                                                        "\n"
                                                        "QToolButton:disabled{\n"
                                                        "    background-color:  gray;\n"
                                                        "    color: white;\n"
                                                        "}")
        self.convertToBlackAndWhiteButton.setCheckable(False)
        self.convertToBlackAndWhiteButton.setObjectName(
            "convertToBlackAndWhiteButton")
        self.verticalLayout_2.addWidget(self.convertToBlackAndWhiteButton)
        self.take2DFastFourierTransformButton = QtWidgets.QToolButton(
            self.imageAnalysisGroupBox)
        self.take2DFastFourierTransformButton.setEnabled(False)
        self.take2DFastFourierTransformButton.setStyleSheet("QToolButton{\n"
                                                            "    background-color: white;\n"
                                                            "    color: black;\n"
                                                            "    font-size: 12px;\n"
                                                            "    width: 220%;\n"
                                                            "    height: 15%;\n"
                                                            "}\n"
                                                            "\n"
                                                            "QToolButton:hover{\n"
                                                            "    background-color:  blue;\n"
                                                            "    color: white;\n"
                                                            "}\n"
                                                            "\n"
                                                            "QToolButton:pressed{\n"
                                                            "    background-color:  white;\n"
                                                            "    color: black;\n"
                                                            "}\n"
                                                            "\n"
                                                            "QToolButton:disabled{\n"
                                                            "    background-color:  gray;\n"
                                                            "    color: white;\n"
                                                            "}")
        self.take2DFastFourierTransformButton.setCheckable(False)
        self.take2DFastFourierTransformButton.setObjectName(
            "take2DFastFourierTransformButton")
        self.verticalLayout_2.addWidget(self.take2DFastFourierTransformButton)
        self.addNoiseGroupBox = QtWidgets.QGroupBox(self.imageAnalysisGroupBox)
        self.addNoiseGroupBox.setObjectName("addNoiseGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.addNoiseGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.addGaussianNoiseButton = QtWidgets.QToolButton(
            self.addNoiseGroupBox)
        self.addGaussianNoiseButton.setEnabled(False)
        self.addGaussianNoiseButton.setStyleSheet("QToolButton{\n"
                                                  "    background-color: white;\n"
                                                  "    color: black;\n"
                                                  "    font-size: 12px;\n"
                                                  "    width: 220%;\n"
                                                  "    height: 15%;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QToolButton:hover{\n"
                                                  "    background-color:  blue;\n"
                                                  "    color: white;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QToolButton:pressed{\n"
                                                  "    background-color:  white;\n"
                                                  "    color: black;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QToolButton:disabled{\n"
                                                  "    background-color:  gray;\n"
                                                  "    color: white;\n"
                                                  "}")
        self.addGaussianNoiseButton.setCheckable(False)
        self.addGaussianNoiseButton.setObjectName("addGaussianNoiseButton")
        self.verticalLayout_3.addWidget(self.addGaussianNoiseButton)
        self.addPepperAndSaltNoiseButton = QtWidgets.QToolButton(
            self.addNoiseGroupBox)
        self.addPepperAndSaltNoiseButton.setEnabled(False)
        self.addPepperAndSaltNoiseButton.setStyleSheet("QToolButton{\n"
                                                       "    background-color: white;\n"
                                                       "    color: black;\n"
                                                       "    font-size: 12px;\n"
                                                       "    width: 220%;\n"
                                                       "    height: 15%;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QToolButton:hover{\n"
                                                       "    background-color:  blue;\n"
                                                       "    color: white;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QToolButton:pressed{\n"
                                                       "    background-color:  white;\n"
                                                       "    color: black;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QToolButton:disabled{\n"
                                                       "    background-color:  gray;\n"
                                                       "    color: white;\n"
                                                       "}")
        self.addPepperAndSaltNoiseButton.setCheckable(False)
        self.addPepperAndSaltNoiseButton.setObjectName(
            "addPepperAndSaltNoiseButton")
        self.verticalLayout_3.addWidget(self.addPepperAndSaltNoiseButton)
        self.verticalLayout_2.addWidget(self.addNoiseGroupBox)
        self.filterGroupBox = QtWidgets.QGroupBox(self.imageAnalysisGroupBox)
        self.filterGroupBox.setObjectName("filterGroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.filterGroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.meanFilterButton = QtWidgets.QToolButton(self.filterGroupBox)
        self.meanFilterButton.setEnabled(False)
        self.meanFilterButton.setStyleSheet("QToolButton{\n"
                                            "    background-color: white;\n"
                                            "    color: black;\n"
                                            "    font-size: 12px;\n"
                                            "    width: 220%;\n"
                                            "    height: 15%;\n"
                                            "}\n"
                                            "\n"
                                            "QToolButton:hover{\n"
                                            "    background-color:  blue;\n"
                                            "    color: white;\n"
                                            "}\n"
                                            "\n"
                                            "QToolButton:pressed{\n"
                                            "    background-color:  white;\n"
                                            "    color: black;\n"
                                            "}\n"
                                            "\n"
                                            "QToolButton:disabled{\n"
                                            "    background-color:  gray;\n"
                                            "    color: white;\n"
                                            "}")
        self.meanFilterButton.setCheckable(False)
        self.meanFilterButton.setObjectName("meanFilterButton")
        self.verticalLayout_4.addWidget(self.meanFilterButton)
        self.medianFilterButton = QtWidgets.QToolButton(self.filterGroupBox)
        self.medianFilterButton.setEnabled(False)
        self.medianFilterButton.setStyleSheet("QToolButton{\n"
                                              "    background-color: white;\n"
                                              "    color: black;\n"
                                              "    font-size: 12px;\n"
                                              "    width: 220%;\n"
                                              "    height: 15%;\n"
                                              "}\n"
                                              "\n"
                                              "QToolButton:hover{\n"
                                              "    background-color:  blue;\n"
                                              "    color: white;\n"
                                              "}\n"
                                              "\n"
                                              "QToolButton:pressed{\n"
                                              "    background-color:  white;\n"
                                              "    color: black;\n"
                                              "}\n"
                                              "\n"
                                              "QToolButton:disabled{\n"
                                              "    background-color:  gray;\n"
                                              "    color: white;\n"
                                              "}")
        self.medianFilterButton.setCheckable(False)
        self.medianFilterButton.setObjectName("medianFilterButton")
        self.verticalLayout_4.addWidget(self.medianFilterButton)
        self.gaussianFilterButton = QtWidgets.QToolButton(self.filterGroupBox)
        self.gaussianFilterButton.setEnabled(False)
        self.gaussianFilterButton.setStyleSheet("QToolButton{\n"
                                                "    background-color: white;\n"
                                                "    color: black;\n"
                                                "    font-size: 12px;\n"
                                                "    width: 220%;\n"
                                                "    height: 15%;\n"
                                                "}\n"
                                                "\n"
                                                "QToolButton:hover{\n"
                                                "    background-color:  blue;\n"
                                                "    color: white;\n"
                                                "}\n"
                                                "\n"
                                                "QToolButton:pressed{\n"
                                                "    background-color:  white;\n"
                                                "    color: black;\n"
                                                "}\n"
                                                "\n"
                                                "QToolButton:disabled{\n"
                                                "    background-color:  gray;\n"
                                                "    color: white;\n"
                                                "}")
        self.gaussianFilterButton.setCheckable(False)
        self.gaussianFilterButton.setObjectName("gaussianFilterButton")
        self.verticalLayout_4.addWidget(self.gaussianFilterButton)
        self.verticalLayout_2.addWidget(self.filterGroupBox)
        self.verticalLayout.addWidget(self.imageAnalysisGroupBox)
        self.edgesButton = QtWidgets.QToolButton(self.sideMenu)
        self.edgesButton.setEnabled(False)
        self.edgesButton.setStyleSheet("QToolButton{\n"
                                       "    background-color: white;\n"
                                       "    color: black;\n"
                                       "    font-size: 12px;\n"
                                       "    width: 220%;\n"
                                       "    height: 15%;\n"
                                       "}\n"
                                       "\n"
                                       "QToolButton:hover{\n"
                                       "    background-color:  blue;\n"
                                       "    color: white;\n"
                                       "}\n"
                                       "\n"
                                       "QToolButton:pressed{\n"
                                       "    background-color:  white;\n"
                                       "    color: black;\n"
                                       "}\n"
                                       "\n"
                                       "QToolButton:disabled{\n"
                                       "    background-color:  gray;\n"
                                       "    color: white;\n"
                                       "}")
        self.edgesButton.setCheckable(False)
        self.edgesButton.setObjectName("edgesButton")
        self.verticalLayout.addWidget(self.edgesButton)
        self.cornersButton = QtWidgets.QToolButton(self.sideMenu)
        self.cornersButton.setEnabled(False)
        self.cornersButton.setStyleSheet("QToolButton{\n"
                                         "    background-color: white;\n"
                                         "    color: black;\n"
                                         "    font-size: 12px;\n"
                                         "    width: 220%;\n"
                                         "    height: 15%;\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:hover{\n"
                                         "    background-color:  blue;\n"
                                         "    color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:pressed{\n"
                                         "    background-color:  white;\n"
                                         "    color: black;\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:disabled{\n"
                                         "    background-color:  gray;\n"
                                         "    color: white;\n"
                                         "}")
        self.cornersButton.setCheckable(False)
        self.cornersButton.setObjectName("cornersButton")
        self.verticalLayout.addWidget(self.cornersButton)
        self.extrasDivider = QtWidgets.QLabel(self.sideMenu)
        self.extrasDivider.setStyleSheet("background-color: red;\n"
                                         "color: white;")
        self.extrasDivider.setText("")
        self.extrasDivider.setAlignment(QtCore.Qt.AlignCenter)
        self.extrasDivider.setObjectName("extrasDivider")
        self.verticalLayout.addWidget(self.extrasDivider)
        self.helpButton = QtWidgets.QToolButton(self.sideMenu)
        self.helpButton.setEnabled(True)
        self.helpButton.setStyleSheet("QToolButton{\n"
                                      "    background-color: white;\n"
                                      "    color: black;\n"
                                      "    font-size: 12px;\n"
                                      "    width: 220%;\n"
                                      "    height: 15%;\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:hover{\n"
                                      "    background-color:  blue;\n"
                                      "    color: white;\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:pressed{\n"
                                      "    background-color:  white;\n"
                                      "    color: black;\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:disabled{\n"
                                      "    background-color:  gray;\n"
                                      "    color: white;\n"
                                      "}")
        self.helpButton.setCheckable(False)
        self.helpButton.setObjectName("helpButton")
        self.verticalLayout.addWidget(self.helpButton)
        self.exitButton = QtWidgets.QToolButton(self.sideMenu)
        self.exitButton.setEnabled(True)
        self.exitButton.setStyleSheet("QToolButton{\n"
                                      "    background-color: white;\n"
                                      "    color: black;\n"
                                      "    font-size: 12px;\n"
                                      "    width: 220%;\n"
                                      "    height: 15%;\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:hover{\n"
                                      "    background-color:  blue;\n"
                                      "    color: white;\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:pressed{\n"
                                      "    background-color:  white;\n"
                                      "    color: black;\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:disabled{\n"
                                      "    background-color:  gray;\n"
                                      "    color: white;\n"
                                      "}")
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        self.verticalLayout_5.addWidget(self.sideMenu)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.imageFrame = QtWidgets.QFrame(self.centralwidget)
        self.imageFrame.setStyleSheet("border: none;")
        self.imageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageFrame.setObjectName("imageFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.imageFrame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.imageLabel = QtWidgets.QLabel(self.imageFrame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMaximumSize(QtCore.QSize(1584, 884))
        self.imageLabel.setAcceptDrops(False)
        self.imageLabel.setText("")
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.verticalLayout_6.addWidget(self.imageLabel)
        self.horizontalLayout_2.addWidget(self.imageFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1064, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exitButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Digital Image Processing Project"))
        self.connectLabel.setText(_translate("MainWindow", "Connect"))
        self.openButton.setText(_translate("MainWindow", "Open"))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.snapButton.setText(_translate("MainWindow", "Snap"))
        self.imageProcessingLabel.setText(
            _translate("MainWindow", "Image Processing"))
        self.loadImageButton.setText(_translate("MainWindow", "Load Image"))
        self.cropAndSaveButton.setText(
            _translate("MainWindow", "Crop and Save"))
        self.imageAnalysisGroupBox.setTitle(
            _translate("MainWindow", "Image Analysis"))
        self.convertToGrayButton.setText(
            _translate("MainWindow", "Convert to Gray"))
        self.convertToBlackAndWhiteButton.setText(
            _translate("MainWindow", "Convert to Black and White"))
        self.take2DFastFourierTransformButton.setText(
            _translate("MainWindow", "Take 2-d fast Fourier Transform"))
        self.addNoiseGroupBox.setTitle(_translate("MainWindow", "Add Noise"))
        self.addGaussianNoiseButton.setText(
            _translate("MainWindow", "Gaussian"))
        self.addPepperAndSaltNoiseButton.setText(
            _translate("MainWindow", "Pepper and Salt"))
        self.filterGroupBox.setTitle(_translate("MainWindow", "Filter"))
        self.meanFilterButton.setText(_translate("MainWindow", "Mean"))
        self.medianFilterButton.setText(_translate("MainWindow", "Median"))
        self.gaussianFilterButton.setText(_translate("MainWindow", "Gaussian"))
        self.edgesButton.setText(_translate("MainWindow", "Edges"))
        self.cornersButton.setText(_translate("MainWindow", "Corners"))
        self.helpButton.setText(_translate("MainWindow", "Help"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
