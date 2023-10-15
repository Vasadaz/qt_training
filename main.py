import sys

from PyQt6 import QtCore, QtGui, QtWidgets

import des

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = des.Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec())
