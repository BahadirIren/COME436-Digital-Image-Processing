"""
    Digital Image Processing Project
    Made By Bahadır İren and Bilal Özdemir
"""


from PyQt5.QtWidgets import *
import Main_Window as mWindow
import sys


app = QApplication(sys.argv)
mainWindow = mWindow.MainWindow()
mainWindow.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
