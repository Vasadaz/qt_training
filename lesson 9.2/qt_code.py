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
        MainWindow.resize(600, 200)
        MainWindow.setMinimumSize(QtCore.QSize(600, 200))
        MainWindow.setMaximumSize(QtCore.QSize(600, 200))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(parent=self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_file = QtGui.QAction(parent=MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionOpen_files = QtGui.QAction(parent=MainWindow)
        self.actionOpen_files.setObjectName("actionOpen_files")
        self.actionOpen_folder = QtGui.QAction(parent=MainWindow)
        self.actionOpen_folder.setObjectName("actionOpen_folder")
        self.actionSave_file = QtGui.QAction(parent=MainWindow)
        self.actionSave_file.setObjectName("actionSave_file")
        self.actionSet_color = QtGui.QAction(parent=MainWindow)
        self.actionSet_color.setObjectName("actionSet_color")
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addAction(self.actionOpen_files)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_folder)
        self.menuFile.addAction(self.actionSave_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSet_color)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionOpen_files.setText(_translate("MainWindow", "Open files"))
        self.actionOpen_folder.setText(_translate("MainWindow", "Open folder"))
        self.actionSave_file.setText(_translate("MainWindow", "Save file"))
        self.actionSet_color.setText(_translate("MainWindow", "Set color"))