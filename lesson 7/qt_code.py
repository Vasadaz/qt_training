# Form implementation generated from reading ui file '.\qt_model.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 200)
        MainWindow.setMinimumSize(QtCore.QSize(380, 200))
        MainWindow.setMaximumSize(QtCore.QSize(380, 200))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PushButtonAddItem = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PushButtonAddItem.setGeometry(QtCore.QRect(10, 70, 171, 23))
        self.PushButtonAddItem.setObjectName("PushButtonAddItem")
        self.PushButtonDeletItems = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PushButtonDeletItems.setGeometry(QtCore.QRect(10, 100, 171, 23))
        self.PushButtonDeletItems.setObjectName("PushButtonDeletItems")
        self.PushButtonChangeProgresBar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PushButtonChangeProgresBar.setGeometry(QtCore.QRect(10, 170, 361, 23))
        self.PushButtonChangeProgresBar.setObjectName("PushButtonChangeProgresBar")
        self.ProgressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.ProgressBar.setGeometry(QtCore.QRect(10, 140, 361, 23))
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ProgressBar.setTextVisible(True)
        self.ProgressBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.ProgressBar.setInvertedAppearance(False)
        self.ProgressBar.setTextDirection(QtWidgets.QProgressBar.Direction.BottomToTop)
        self.ProgressBar.setObjectName("ProgressBar")
        self.LineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LineEdit.setGeometry(QtCore.QRect(10, 40, 171, 20))
        self.LineEdit.setText("")
        self.LineEdit.setObjectName("LineEdit")
        self.PlainTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.PlainTextEdit.setGeometry(QtCore.QRect(190, 9, 180, 111))
        self.PlainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.PlainTextEdit.setAccessibleName("")
        self.PlainTextEdit.setPlainText("")
        self.PlainTextEdit.setCenterOnScroll(False)
        self.PlainTextEdit.setObjectName("PlainTextEdit")
        self.ComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.ComboBox.setGeometry(QtCore.QRect(10, 10, 170, 22))
        self.ComboBox.setObjectName("ComboBox")
        self.ComboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PushButtonAddItem.setText(_translate("MainWindow", "Добавить значение"))
        self.PushButtonDeletItems.setText(_translate("MainWindow", "Удалить все значения"))
        self.PushButtonChangeProgresBar.setText(_translate("MainWindow", "Изменить стиль ProgresBar"))
        self.ProgressBar.setFormat(_translate("MainWindow", "%p%"))
        self.LineEdit.setPlaceholderText(_translate("MainWindow", "Введите значение"))
        self.PlainTextEdit.setPlaceholderText(_translate("MainWindow", "Лог программы..."))
        self.ComboBox.setItemText(0, _translate("MainWindow", "example"))
