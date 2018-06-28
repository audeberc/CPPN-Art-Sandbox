# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anim_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_anim_window(object):
    def setupUi(self, anim_window):
        anim_window.setObjectName("anim_window")
        anim_window.resize(520, 127)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(anim_window.sizePolicy().hasHeightForWidth())
        anim_window.setSizePolicy(sizePolicy)
        self.buttonBox = QtWidgets.QDialogButtonBox(anim_window)
        self.buttonBox.setGeometry(QtCore.QRect(130, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(anim_window)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.min_A_box = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.min_A_box.setDecimals(2)
        self.min_A_box.setMinimum(-100.0)
        self.min_A_box.setMaximum(100.0)
        self.min_A_box.setSingleStep(0.1)
        self.min_A_box.setProperty("value", -0.5)
        self.min_A_box.setObjectName("min_A_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.min_A_box)
        self.frame_bpx = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.frame_bpx.setMinimum(1)
        self.frame_bpx.setMaximum(2000)
        self.frame_bpx.setProperty("value", 240)
        self.frame_bpx.setObjectName("frame_bpx")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.frame_bpx)
        self.max_A_box = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.max_A_box.setDecimals(2)
        self.max_A_box.setMinimum(-100.0)
        self.max_A_box.setMaximum(100.0)
        self.max_A_box.setSingleStep(0.1)
        self.max_A_box.setProperty("value", 2.0)
        self.max_A_box.setObjectName("max_A_box")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.max_A_box)

        self.retranslateUi(anim_window)
        self.buttonBox.accepted.connect(anim_window.accept)
        self.buttonBox.rejected.connect(anim_window.reject)
        QtCore.QMetaObject.connectSlotsByName(anim_window)

    def retranslateUi(self, anim_window):
        _translate = QtCore.QCoreApplication.translate
        anim_window.setWindowTitle(_translate("anim_window", "Dialog"))
        self.label_2.setText(_translate("anim_window", "Max A value"))
        self.label_3.setText(_translate("anim_window", "Number of frames"))
        self.label.setText(_translate("anim_window", "Min A value"))

