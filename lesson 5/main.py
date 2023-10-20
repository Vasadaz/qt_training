import sys

from PyQt6 import QtWidgets

import qt_code


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = qt_code.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.handler)
        self.ui.checkBox.clicked.connect(self.handler_checkbox)
        self.ui.radioButton.clicked.connect(self.handler_radio)

    def handler(self):
        checkbox = ' CHECK '
        radio = ' RADIO '
        if self.ui.checkBox.isChecked():
            checkbox += self.ui.checkBox.text()

        if self.ui.checkBox_2.isChecked():
            checkbox += self.ui.checkBox_2.text()

        if self.ui.radioButton.isChecked():
            radio += self.ui.radioButton.text()

        elif self.ui.radioButton_2.isChecked():
            radio += self.ui.radioButton_2.text()

        self.ui.plainTextEdit.appendPlainText('text' + checkbox + radio)
        self.ui.pushButton.setText('STOP')
        self.ui.pushButton.setStyleSheet('background-color: #E74D25; color: white;')
        print('work')

    def handler_radio(self):
        self.ui.plainTextEdit.appendPlainText('I Radio')
        self.ui.radioButton_2.setText('***')

    def handler_checkbox(self):
        self.ui.plainTextEdit.appendPlainText('I CHECK')

    def setcolor(self):
        self.ui.pushButton.setDisabled(False)
        self.ui.pushButton.setText('GO')
        self.ui.pushButton.setStyleSheet('background-color: #00E000; color: white;')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec())
