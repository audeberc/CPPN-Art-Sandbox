# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.imgsetting_button = QtWidgets.QPushButton(self.centralWidget)
        self.imgsetting_button.setObjectName("imgsetting_button")
        self.gridLayout.addWidget(self.imgsetting_button, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rndseed_button = QtWidgets.QPushButton(self.centralWidget)
        self.rndseed_button.setObjectName("rndseed_button")
        self.horizontalLayout.addWidget(self.rndseed_button)
        self.rndseed_edit = QtWidgets.QLineEdit(self.centralWidget)
        self.rndseed_edit.setObjectName("rndseed_edit")
        self.horizontalLayout.addWidget(self.rndseed_edit)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.var_edit = QtWidgets.QLineEdit(self.centralWidget)
        self.var_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.var_edit.setObjectName("var_edit")
        self.gridLayout.addWidget(self.var_edit, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.animA_button = QtWidgets.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.animA_button.setFont(font)
        self.animA_button.setObjectName("animA_button")
        self.horizontalLayout_3.addWidget(self.animA_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.y_edit = QtWidgets.QLineEdit(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.y_edit.setFont(font)
        self.y_edit.setObjectName("y_edit")
        self.gridLayout_2.addWidget(self.y_edit, 1, 1, 1, 1)
        self.A_edit = QtWidgets.QLineEdit(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.A_edit.setFont(font)
        self.A_edit.setObjectName("A_edit")
        self.gridLayout_2.addWidget(self.A_edit, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.x_edit = QtWidgets.QLineEdit(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.x_edit.setFont(font)
        self.x_edit.setObjectName("x_edit")
        self.gridLayout_2.addWidget(self.x_edit, 1, 0, 1, 1)
        self.z_edit = QtWidgets.QLineEdit(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.z_edit.setFont(font)
        self.z_edit.setObjectName("z_edit")
        self.gridLayout_2.addWidget(self.z_edit, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.addlayer_button = QtWidgets.QPushButton(self.centralWidget)
        self.addlayer_button.setObjectName("addlayer_button")
        self.gridLayout.addWidget(self.addlayer_button, 7, 0, 1, 1)
        self.layer_list = QtWidgets.QListWidget(self.centralWidget)
        self.layer_list.setLineWidth(2)
        self.layer_list.setResizeMode(QtWidgets.QListView.Fixed)
        self.layer_list.setModelColumn(0)
        self.layer_list.setUniformItemSizes(True)
        self.layer_list.setObjectName("layer_list")
        self.gridLayout.addWidget(self.layer_list, 6, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.img_label = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.img_label.sizePolicy().hasHeightForWidth())
        self.img_label.setSizePolicy(sizePolicy)
        self.img_label.setSizeIncrement(QtCore.QSize(10, 10))
        self.img_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img_label.setText("")
        self.img_label.setObjectName("img_label")
        self.verticalLayout.addWidget(self.img_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.preview_button = QtWidgets.QPushButton(self.centralWidget)
        self.preview_button.setObjectName("preview_button")
        self.horizontalLayout_2.addWidget(self.preview_button)
        self.render_button = QtWidgets.QPushButton(self.centralWidget)
        self.render_button.setObjectName("render_button")
        self.horizontalLayout_2.addWidget(self.render_button)
        self.export_button = QtWidgets.QPushButton(self.centralWidget)
        self.export_button.setObjectName("export_button")
        self.horizontalLayout_2.addWidget(self.export_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setEnabled(False)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1080, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setEnabled(False)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setEnabled(False)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.imgsetting_button.setText(_translate("MainWindow", "Image settings"))
        self.rndseed_button.setText(_translate("MainWindow", "RND"))
        self.rndseed_edit.setText(_translate("MainWindow", "SEED"))
        self.var_edit.setText(_translate("MainWindow", "50"))
        self.var_edit.setPlaceholderText(_translate("MainWindow", "Variance"))
        self.label_5.setText(_translate("MainWindow", "Variance"))
        self.label.setText(_translate("MainWindow", "A"))
        self.animA_button.setText(_translate("MainWindow", "Anim"))
        self.label_2.setText(_translate("MainWindow", "X"))
        self.y_edit.setText(_translate("MainWindow", "y"))
        self.A_edit.setText(_translate("MainWindow", "0.5"))
        self.label_3.setText(_translate("MainWindow", "Y"))
        self.label_4.setText(_translate("MainWindow", "Z"))
        self.x_edit.setText(_translate("MainWindow", "x"))
        self.z_edit.setText(_translate("MainWindow", "sqrt(x**2+y**2)"))
        self.addlayer_button.setText(_translate("MainWindow", "Add Layer"))
        self.preview_button.setText(_translate("MainWindow", "Preview"))
        self.render_button.setText(_translate("MainWindow", "Render"))
        self.export_button.setText(_translate("MainWindow", "Export"))

