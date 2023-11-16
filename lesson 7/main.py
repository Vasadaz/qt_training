import sys

from PyQt6 import QtGui, QtWidgets

import qt_code


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = qt_code.Ui_MainWindow()
        self.ui.setupUi(self)

        self.progress_flag = False
        self.progress_value = 0
        self.ui.ProgressBar.setValue(self.progress_value)

        self.ui.PushButtonAddItem.clicked.connect(self.add_item)
        self.ui.PushButtonDeletItems.clicked.connect(self.clear_box)
        self.ui.PushButtonChangeProgresBar.clicked.connect(self.set_style)

    def add_item(self):

        if self.ui.LineEdit.text():
            if self.ui.ProgressBar.value() == 100:
                self.ui.PlainTextEdit.clear()
                self.ui.PlainTextEdit.appendPlainText('Список заполнен!')
                return

            line_text = self.ui.LineEdit.text()
            elements_count = self.ui.ComboBox.count()

            for element in range(0, elements_count):
                self.ui.ComboBox.setCurrentIndex(element)
                local_text = self.ui.ComboBox.currentText()

                if local_text == line_text:
                    error_message = 'Объект уже существует!'
                    self.ui.PlainTextEdit.appendPlainText(error_message)
                    return

            self.progress_value += 10
            self.ui.ComboBox.addItem(line_text)
            self.ui.PlainTextEdit.appendPlainText('Объект добавлен')
            self.ui.ProgressBar.setValue(self.progress_value)
        else:
            self.ui.PlainTextEdit.appendPlainText('Строка не может быть пустой!')

    def clear_box(self):
        self.progress_value = 0
        self.ui.ComboBox.clear()
        self.ui.PlainTextEdit.clear()
        self.ui.PlainTextEdit.appendPlainText('Все объекты удалены')
        self.ui.ProgressBar.setValue(self.progress_value)

    def set_style(self):
        default_style = '''
            QProgressBar{
            }
        '''

        style = '''
            QProgressBar::chunk {
                border-radius:11px;
                background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 #01FAFF,stop:1  #26B4FF);
            }
            QProgressBar#progressBar {
                height: 22px;
                Text-align: center; / * Text location * /
                font-size: 14px;
                color: white;
                border-radius: 11px;
                background: #1D5573;
            }
        '''

        if not self.progress_flag:
            self.ui.ProgressBar.setStyleSheet(style)
            self.progress_flag = True
        else:
            self.ui.ProgressBar.setStyleSheet(default_style)
            self.progress_flag = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec())
