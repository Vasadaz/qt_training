import sys

from PyQt6 import QtCore, QtWidgets

import qt_code


class Handler(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        self.signal.emit('Какое-то значение...')


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = qt_code.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_handler)

        self.mythread = Handler()
        self.mythread.signal.connect(self.add_item)

    def start_handler(self):
        self.mythread.start()

    def add_item(self, value):
        self.ui.textBrowser.append(value)

    def closeEvent(self, value):
        if self.open_modal_window():
            super().__init__(self).closeEvent(value)
        value.ignore()

    def open_modal_window(self):
        modal_window2 = QtWidgets.QWidget(self, QtCore.Qt.WindowType.Window)
        result = QtWidgets.QMessageBox.question(
            self,
            'Закрытие окна',
            'Вы действительно хотите закрыть окно?',
            QtWidgets.QMessageBox.StandardButton.Yes,
            QtWidgets.QMessageBox.StandardButton.No,
        )

        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            return True
        return False

    def event(self, e):
        if e.type() == QtCore.QEvent.Type.KeyPress:
            text = f'Нажата клавиша {e.text()}'
            self.ui.textBrowser.append(text)
        elif e.type() == QtCore.QEvent.Type.MouseButtonPress:
            text = f'Координаты нажатия мышки X={e.pos().x()} Y={e.pos().y()}'
            self.ui.textBrowser.append(text)
        return QtWidgets.QWidget.event(self, e)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec())
