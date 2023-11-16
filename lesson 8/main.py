import sys

from PyQt6 import QtGui, QtWidgets

import qt_code


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = qt_code.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.notifications)
        self.ui.pushButton_2.clicked.connect(self.confirm)
        self.ui.pushButton_3.clicked.connect(self.message)

    def notifications(self):
        QtWidgets.QMessageBox.about(self, 'title', 'message')
        QtWidgets.QMessageBox.warning(self, 'title', 'message')
        QtWidgets.QMessageBox.information(self, 'title', 'message')
        QtWidgets.QMessageBox.critical(self, 'title', 'message')

    def confirm(self):
        result = QtWidgets.QMessageBox.question(
            self,
            'Headers',
            'Description...',
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No,
            #QtWidgets.QMessageBox.,
        )

    def message(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg.setWindowTitle('title')
        msg.setInformativeText('description')
        msg.setDetailedText('detail')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        item = msg.exec()

        if item == QtWidgets.QMessageBox.Ok:
            print('OK')
        elif item == QtWidgets.QMessageBox.Cancel:
            print('CANCEL')

    def error_message(self):
        error = QtWidgets.QErrorMessage(self)
        error.setWindowTitle('title')
        error.showMessage('error message')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec())
