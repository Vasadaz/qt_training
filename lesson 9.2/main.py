import sys

from PyQt6 import QtWidgets

import qt_code


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = qt_code.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpen_file.triggered.connect(self.open_file)
        self.ui.actionSave_file.triggered.connect(self.save_file)
        self.ui.actionOpen_files.triggered.connect(self.open_files)
        self.ui.actionSet_color.triggered.connect(self.set_color)
        self.ui.actionOpen_folder.triggered.connect(self.open_folder)

    def open_file(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'headers',
            'filename',
            'Python *.py\nImage (*.png *.jpeg)',
        )
        print(file_path)
        self.ui.statusbar.showMessage(file_path[0])

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
        self.ui.statusbar.showMessage(file_path[0])

    def open_files(self):
        file_paths = QtWidgets.QFileDialog.getOpenFileNames(
            self,
            'headers',
            'filename_for_save',
            'Python *.py\nImage (*.png, *.jpeg)',
        )
        print(file_paths)
        self.ui.statusbar.showMessage(', '.join(file_paths[0]))

    def open_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self)
        print(directory)
        self.ui.statusbar.showMessage(directory[0])

    def set_color(self):
        color = QtWidgets.QColorDialog(self).getColor()
        print(color.red(), color.green(), color.blue(), color.alpha())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec())
