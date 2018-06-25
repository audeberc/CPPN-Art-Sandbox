# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_settings.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_image_setting_dialog(object):
    def setupUi(self, image_setting_dialog):
        image_setting_dialog.setObjectName("image_setting_dialog")
        image_setting_dialog.resize(415, 193)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(image_setting_dialog.sizePolicy().hasHeightForWidth())
        image_setting_dialog.setSizePolicy(sizePolicy)
        self.buttonBox = QtWidgets.QDialogButtonBox(image_setting_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(image_setting_dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 351, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.preview_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.preview_edit.setObjectName("preview_edit")
        self.gridLayout.addWidget(self.preview_edit, 0, 1, 1, 1)
        self.render_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.render_edit.setObjectName("render_edit")
        self.gridLayout.addWidget(self.render_edit, 1, 1, 1, 1)

        self.retranslateUi(image_setting_dialog)
        self.buttonBox.accepted.connect(image_setting_dialog.accept)
        self.buttonBox.rejected.connect(image_setting_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(image_setting_dialog)

    def retranslateUi(self, image_setting_dialog):
        _translate = QtCore.QCoreApplication.translate
        image_setting_dialog.setWindowTitle(_translate("image_setting_dialog", "Image settings"))
        self.label.setText(_translate("image_setting_dialog", "Render width"))
        self.label_2.setText(_translate("image_setting_dialog", "Preview width"))
        self.preview_edit.setText(_translate("image_setting_dialog", "64"))
        self.render_edit.setText(_translate("image_setting_dialog", "1024"))
