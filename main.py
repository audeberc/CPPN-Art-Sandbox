from GUI.mainwindow import Ui_MainWindow
from GUI.image_settings import Ui_image_setting_dialog
from GUI.layer_item import Ui_Form
from math import *

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from GUI import style
import sys
import random

from keras.layers import Input, Dense
from keras.models import Model
from keras import initializers

class CPPNApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        sshFile = "./style.qss"
        self.setStyleSheet(style.stylesheet)
        ### Default settings
        self.preview_res = 64
        self.render_res = 1024
        self.random_seed()
        self.variance = 50
        self.Xfunc = lambda x: x
        self.Yfunc = lambda y: y
        self.Zfunc = lambda x, y : sqrt(x**2+y**2)
        self.A = 0.5
        self.unit_list = []
        self.activation_list = []
        ### Signal init
        # Img menu
        self.imgsetting_button.clicked.connect(self.open_img_settings)
        self.settings_dialog =  QtWidgets.QDialog()
        self.settings_dialog.ui = Ui_image_setting_dialog()
        self.settings_dialog.ui.setupUi(self.settings_dialog)
        self.settings_dialog.ui.buttonBox.accepted.connect(self.save_img_settings)
        # RND
        self.rndseed_button.clicked.connect(self.random_seed)
        self.rndseed_edit.textChanged.connect(self.manual_seed)
        # Variance
        self.var_edit.textChanged.connect(self.set_variance)

        self.x_edit.textChanged.connect(self.set_Xfunc)
        self.y_edit.textChanged.connect(self.set_Yfunc)
        self.z_edit.textChanged.connect(self.set_Zfunc)
        self.A_edit.textChanged.connect(self.set_A)
        self.add_layer()
        self.add_layer()
        self.add_layer()
        self.addlayer_button.clicked.connect(self.add_layer)
        self.layer_list.itemDoubleClicked.connect(self.remove_layer)

        self.preview_button.clicked.connect(self.build_network)

    def open_img_settings(self):
        self.settings_dialog.ui.preview_edit.setText(str(self.preview_res))
        self.settings_dialog.ui.render_edit.setText(str(self.render_res ))
        self.settings_dialog.show()

    def save_img_settings(self):
        self.preview_res = self.settings_dialog.ui.preview_edit.text()
        self.render_res = self.settings_dialog.ui.render_edit.text()

    def random_seed(self):
        self.seed = random.getrandbits(32)
        self.rndseed_edit.setText(str(self.seed))

    def manual_seed(self):
        self.seed = self.rndseed_edit.text()

    def set_variance(self):
        self.variance = self.var_edit.text()

    def set_Xfunc(self):
        if "x" in self.x_edit.text():
            self.Xfunc = lambda x: eval(self.x_edit.text())

    def set_Yfunc(self):
        if "y" in self.y_edit.text():
            self.Yfunc = lambda y : eval(self.y_edit.text())

    def set_Zfunc(self):
        if "z" in self.z_edit.text():
            self.Zfunc = lambda x, y : eval(self.z_edit.text())

    def set_A(self):
        self.A = float(self.A_edit.text())

    def add_layer(self):
        new_line =  QtWidgets.QDialog()
        new_line.ui = Ui_Form()
        new_line.ui.setupUi(new_line)
        item = QtWidgets.QListWidgetItem(self.layer_list)
        item.setSizeHint(QtCore.QSize(30,30))
        self.unit_list.append(new_line.ui.units_combo)
        self.activation_list.append(new_line.ui.activation_combo)
        self.layer_list.addItem(item)
        self.layer_list.setItemWidget(item, new_line )

    def remove_layer(self, item):
        self.layer_list.takeItem(self.layer_list.count()-1)
        del self.unit_list[-1]
        del self.activation_list[-1]

    def build_network(self):
        initialisation = initializers.VarianceScaling(scale=self.variance, distribution="normal", seed=self.seed)
        inputs = Input(shape=(4,))
        x = inputs
        for layer_number in range(self.layer_list.count()):
            x = Dense(self.unit_list[layer_number].value(), activation=self.activation_list[layer_number].currentText(), kernel_initializer=initialisation)(x)
        output = Dense(3, activation='linear', kernel_initializer=initialisation)(x)
        model = Model(inputs=inputs, outputs=output)

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = CPPNApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
