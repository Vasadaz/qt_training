import sys

from PyQt6 import QtCore, QtWidgets

import qt_code
import qt_code_wiget


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = qt_code.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_modal_window)
        self.ui.pushButton_2.clicked.connect(self.open_modal_window2)

    def open_modal_window(self):
        window = ModalWindow(self)
        window.show()

    def open_modal_window2(self):
        modal_window2 = QtWidgets.QWidget(self, QtCore.Qt.WindowType.Window)
        modal_window2.setWindowTitle('ModalW2')
        modal_window2.resize(300, 500)
        modal_window2.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        modal_window2.show()


class ModalWindow(QtWidgets.QWidget):
    def __init__(self, parent=GUI):
        super().__init__(parent, QtCore.Qt.WindowType.Window)
        self.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        self.ui = qt_code_wiget.Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec())
