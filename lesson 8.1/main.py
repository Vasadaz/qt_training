import sys

from PyQt6 import QtWidgets

import qt_code


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = qt_code.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.notifications)
        self.ui.pushButton_2.clicked.connect(self.confirm)
        self.ui.pushButton_3.clicked.connect(self.message)
        self.ui.pushButton_4.clicked.connect(self.error_message)

    def notifications(self):
        # QtWidgets.QMessageBox.about(self, 'title', 'message')
        # QtWidgets.QMessageBox.warning(self, 'title', 'message')
        QtWidgets.QMessageBox.information(self, 'title', 'message')
        # QtWidgets.QMessageBox.critical(self, 'title', 'message')

    def confirm(self):
        result = QtWidgets.QMessageBox.question(
            self,
            'Headers',
            'Description...',
            QtWidgets.QMessageBox.StandardButton.Yes,
            QtWidgets.QMessageBox.StandardButton.No,
            # QtWidgets.QMessageBox.,
        )

        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            print('Yes')
        else:
            print('No')

    @staticmethod
    def message():
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setWindowTitle('title')
        msg.setInformativeText('description')
        msg.setDetailedText('detail')
        msg.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Ok |
            QtWidgets.QMessageBox.StandardButton.Cancel |
            QtWidgets.QMessageBox.StandardButton.Help
        )
        item = msg.exec()
        print(item.real)

        if item == QtWidgets.QMessageBox.StandardButton.Ok:
            print('OK')
        elif item == QtWidgets.QMessageBox.StandardButton.Cancel:
            print('CANCEL')
        else:
            print('HELP')

    def error_message(self):
        error = QtWidgets.QErrorMessage(self)
        error.setWindowTitle('title')
        error.showMessage('error message')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec())
