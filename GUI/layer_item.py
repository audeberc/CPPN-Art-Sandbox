# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/layer_item.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(223, 28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 28))
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 223, 36))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.activation_combo = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.activation_combo.setMinimumSize(QtCore.QSize(0, 26))
        self.activation_combo.setIconSize(QtCore.QSize(16, 9))
        self.activation_combo.setObjectName("activation_combo")
        self.activation_combo.addItem("")
        self.activation_combo.addItem("")
        self.activation_combo.addItem("")
        self.activation_combo.addItem("")
        self.activation_combo.addItem("")
        self.activation_combo.addItem("")
        self.horizontalLayout.addWidget(self.activation_combo)
        self.units_combo = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.units_combo.setMinimum(3)
        self.units_combo.setMaximum(2048)

        self.units_combo.setProperty("value", 16)
        self.units_combo.setObjectName("units_combo")
        self.horizontalLayout.addWidget(self.units_combo)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.activation_combo.setItemText(0, _translate("Form", "tanh"))
        self.activation_combo.setItemText(1, _translate("Form", "softmax"))
        self.activation_combo.setItemText(2, _translate("Form", "sigmoid"))
        self.activation_combo.setItemText(3, _translate("Form", "linear"))
        self.activation_combo.setItemText(4, _translate("Form", "elu"))
        self.activation_combo.setItemText(5, _translate("Form", "relu"))
