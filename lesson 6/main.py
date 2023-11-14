import sys

from PyQt6 import QtGui, QtWidgets

import qt_code


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = qt_code.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ICON_NUM = 0
        self.ui.pushButton.clicked.connect(self.add_item)
        self.ui.pushButton_2.clicked.connect(self.clear_all_item)

        self.TABLE_INDEX = 0
        self.ROW_COUNT = 1
        self.ui.pushButton_3.clicked.connect(self.add_table_item)
        self.ui.pushButton_4.clicked.connect(self.clear_table)

    def add_item(self):
        radio_buttons = [
            self.ui.radioButton,
            self.ui.radioButton_2,
            self.ui.radioButton_3,
            self.ui.radioButton_4,
        ]

        for radio_button in radio_buttons:
            if radio_button.isChecked():
                name = radio_button.text().strip('#')
                icon = QtGui.QIcon(f'icons/{name}.png')
                self.ui.listWidget.addItem(f'{name} - {self.ICON_NUM}')
                self.ui.listWidget.setCurrentRow(self.ICON_NUM)
                item = self.ui.listWidget.currentItem()
                item.setIcon(icon)

                self.ICON_NUM += 1

    def add_table_item(self):
        user_id = ''
        user_name = ''
        user_age = ''

        if self.ui.lineEdit.text() and self.ui.lineEdit_2.text() and self.ui.lineEdit_3.text():
            user_id = self.ui.lineEdit.text()
            user_name = self.ui.lineEdit_2.text()
            user_age = self.ui.lineEdit_3.text()

            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()

        else:
            return

        self.ui.tableWidget.setRowCount(self.ROW_COUNT)
        self.ui.tableWidget.setItem(self.TABLE_INDEX, 0, QtWidgets.QTableWidgetItem(user_id))
        self.ui.tableWidget.setItem(self.TABLE_INDEX, 1, QtWidgets.QTableWidgetItem(user_name))
        self.ui.tableWidget.setItem(self.TABLE_INDEX, 2, QtWidgets.QTableWidgetItem(user_age))

        self.ROW_COUNT += 1
        self.TABLE_INDEX += 1

    def clear_all_item(self):
        self.ui.listWidget.clear()
        self.ICON_NUM = 0

    def clear_table(self):
        self.ROW_COUNT = 0
        self.TABLE_INDEX = 1
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('ID'))
        self.ui.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('NAME'))
        self.ui.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('AGE'))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec())
