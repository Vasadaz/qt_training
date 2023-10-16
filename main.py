import sys
import time

from PyQt6 import QtCore, QtGui, QtWidgets

import des

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = des.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.handler)
        self.ui.pushButton_2.clicked.connect(self.setcolor)

    def handler(self):
        self.ui.pushButton.setDisabled(True)
        self.ui.plainTextEdit.appendPlainText('text')
        self.ui.label.setText('DONE!')
        self.ui.pushButton.setText('STOP')
        self.ui.pushButton.setStyleSheet('background-color: #E74D25; color: white;')
        print('work')


    def setcolor(self):
        self.ui.pushButton.setDisabled(False)
        self.ui.pushButton.setText('GO')
        self.ui.pushButton.setStyleSheet('background-color: #00E000; color: white;')




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec())
