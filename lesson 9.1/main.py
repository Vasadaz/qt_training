import sys

from PyQt6 import QtWidgets

import qt_code


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = qt_code.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_file)
        self.ui.pushButton_2.clicked.connect(self.save_file)
        self.ui.pushButton_3.clicked.connect(self.open_files)
        self.ui.pushButton_4.clicked.connect(self.set_color)
        self.ui.pushButton_5.clicked.connect(self.open_folder)

    def open_file(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'headers',
            'filename',
            'Python *.py\nImage (*.png *.jpeg)',
        )
        print(file_path)

    def save_file(self):
        file_path = QtWidgets.QFileDialog.getSaveFileName(
            self,
            'headers',
            'filename_for_save',
            'Python *.py\nDocument (*.txt *.md)',
        )

        with open(file_path[0], 'w') as file:
            file.write('My New File!!')

        print(file_path)

    def open_files(self):
        file_paths = QtWidgets.QFileDialog.getOpenFileNames(
            self,
            'headers',
            'filename_for_save',
            'Python *.py\nImage (*.png, *.jpeg)',
        )
        print(file_paths)

    def open_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self)
        print(directory)

    def set_color(self):
        color = QtWidgets.QColorDialog(self).getColor()
        print(color.red(), color.green(), color.blue(), color.alpha())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec())
