from GUI.mainwindow import Ui_MainWindow
from GUI.image_settings import Ui_image_setting_dialog
from GUI.layer_item import Ui_Form
from GUI.anim_window import Ui_anim_window
from math import *
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import numpy as np
from GUI import style
import sys
import random

from keras.layers import Input, Dense
from keras.models import Model
from keras import initializers
from skimage.color import hsv2rgb


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
        self.final_render = []
        self.maxA = -2.0
        self.minA = 2.0
        self.anim_frames = 240
        ### Signal init
        # Img menu
        self.imgsetting_button.clicked.connect(self.open_img_settings)
        self.settings_dialog =  QtWidgets.QDialog()
        self.settings_dialog.ui = Ui_image_setting_dialog()
        self.settings_dialog.ui.setupUi(self.settings_dialog)
        self.settings_dialog.ui.buttonBox.accepted.connect(self.save_img_settings)
        # Anim menu
        self.animA_button.clicked.connect(self.open_anim_settings)
        self.anim_dialog =  QtWidgets.QDialog()
        self.anim_dialog.ui = Ui_anim_window()
        self.anim_dialog.ui.setupUi(self.anim_dialog)
        self.anim_dialog.ui.buttonBox.accepted.connect(self.anim)
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
        self.preview_button.clicked.connect(self.preview)
        self.export_button.clicked.connect(self.export)
        self.render_button.clicked.connect(self.render_final)

    def open_img_settings(self):
        self.settings_dialog.ui.preview_edit.setText(str(self.preview_res))
        self.settings_dialog.ui.render_edit.setText(str(self.render_res ))
        self.settings_dialog.show()

    def open_anim_settings(self):
        self.anim_dialog.ui.min_A_box.setValue((self.maxA))
        self.anim_dialog.ui.max_A_box.setValue((self.minA))
        self.anim_dialog.ui.frame_bpx.setValue((self.anim_frames))
        self.anim_dialog.show()

    def save_img_settings(self):
        self.preview_res = int(self.settings_dialog.ui.preview_edit.text())
        self.render_res = int(self.settings_dialog.ui.render_edit.text())

    def random_seed(self):
        self.seed = int(random.getrandbits(32))
        self.rndseed_edit.setText(str(self.seed))

    def manual_seed(self):
        self.seed = self.rndseed_edit.text()

    def set_variance(self):
        self.variance = float(self.var_edit.text())

    def set_Xfunc(self):
        if "x" in self.x_edit.text():
            self.Xfunc = lambda x: eval(self.x_edit.text())

    def set_Yfunc(self):
        if "y" in self.y_edit.text():
            self.Yfunc = lambda y : eval(self.y_edit.text())

    def set_Zfunc(self):
        if "x" in self.z_edit.text() or "y" in self.z_edit.text():
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
        initialisation = initializers.VarianceScaling(scale=self.variance, distribution="normal", seed=int(self.seed))
        inputs = Input(shape=(4,))
        x = inputs
        for layer_number in range(self.layer_list.count()):
            x = Dense(self.unit_list[layer_number].value(), activation=self.activation_list[layer_number].currentText(), kernel_initializer=initialisation)(x)
        output = Dense(3, activation='linear', kernel_initializer=initialisation)(x)
        self.model = Model(inputs=inputs, outputs=output)

    def build_img_grid(self, x_size, y_size, alpha = 1.0, scale=1.0, f1=(lambda x:x), f2=(lambda x:x), f3=(lambda x,y : sqrt(x**2+y**2))):
        X, Y = np.meshgrid(np.linspace(-scale,scale,x_size), np.linspace(-scale,scale,y_size), indexing='ij')
        V = [[f1(x), f2(y), f3(x,y), alpha] for x,y in zip(np.ravel(X),np.ravel(Y))]
        return np.array(V)

    def render_img(self, model, vector_shape = (20,20), scale=2.0, alpha = 0.50, grid_functs = [(lambda x:x), (lambda x:x), (lambda x,y : sqrt(x**2+y**2))]):
        V = self.build_img_grid(vector_shape[0], vector_shape[1], scale=scale, alpha=alpha,
                              f1=grid_functs[0],
                              f2=grid_functs[1],
                              f3=grid_functs[2])
        model.compile(optimizer='adam', loss='mse')
        pred = model.predict(V)

        img = []
        for i in range(pred.shape[1]):
            channel = pred[:, i]
            norm = (channel - channel.min()) / (channel.max()-channel.min())
            img.append(norm.reshape(vector_shape))
        img = np.dstack(img)

        return hsv2rgb(((255.0*img)).astype(np.uint8))

    def preview(self):
        self.build_network()
        preview = 255*self.render_img(self.model, (self.preview_res, self.preview_res), alpha=self.A, grid_functs=[self.Xfunc,self.Yfunc,self.Zfunc])

        preview = cv2.resize(preview, (1024, 1024), interpolation=cv2.INTER_CUBIC)

        nimage = QtGui.QImage(preview[..., ::-1].astype(np.uint8), 1024, 1024, 1024*3,QtGui.QImage.Format_RGB888)
        nimage.ndarray = preview
        pix = QtGui.QPixmap(nimage)
        self.img_label.setPixmap(pix)

    def render_final(self):

        splash_pix = QtGui.QPixmap('GUI/loading.png')
        splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
        splash.show()
        QtCore.QCoreApplication.processEvents()
        self.build_network()
        QtCore.QCoreApplication.processEvents()
        final = 255*self.render_img(self.model, (self.render_res, self.render_res), alpha=self.A, grid_functs=[self.Xfunc,self.Yfunc,self.Zfunc])

        final = cv2.resize(final, (1024, 1024), interpolation=cv2.INTER_CUBIC)
        nimage = QtGui.QImage(final[..., ::-1].astype(np.uint8), 1024, 1024, 1024*3,QtGui.QImage.Format_RGB888)
        nimage.ndarray = final
        pix = QtGui.QPixmap(nimage)
        self.img_label.setPixmap(pix)
        self.final_render = final
        QtCore.QCoreApplication.processEvents()
        splash.close()

    def export(self):
        self.output_path = str(QtWidgets.QFileDialog.getSaveFileName(self)[0])
        cv2.imwrite(self.output_path, self.final_render)

    def anim(self):

        self.maxA = self.anim_dialog.ui.min_A_box.value()
        self.minA = self.anim_dialog.ui.max_A_box.value()
        self.anim_frames = self.anim_dialog.ui.frame_bpx.value()
        self.output_folder = str(QtWidgets.QFileDialog.getExistingDirectory(None, 'Select a folder:', None, QtWidgets.QFileDialog.ShowDirsOnly))
        QtCore.QCoreApplication.processEvents()
        load = LoadScreen(self.anim_frames)
        load.show()
        alphas = np.linspace(self.minA,self.maxA,self.anim_frames)
        QtCore.QCoreApplication.processEvents()
        for i in range(self.anim_frames):
            QtCore.QCoreApplication.processEvents()
            load.progressBar.setValue(i)
            self.build_network()
            render_i = 255*self.render_img(self.model, (self.render_res, self.render_res), alpha=alphas[i], grid_functs=[self.Xfunc,self.Yfunc,self.Zfunc])
            cv2.imwrite(self.output_folder+"/"+str(i)+".png", render_i)


class LoadScreen( QtWidgets.QWidget) :
    def __init__(self, maxvalue, parent = None) :
        super().__init__( parent)
        self.setObjectName("Loading")
        self.parent = parent

        #progress bar
        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setObjectName("Loading...")

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setObjectName("Loading layout")
        self.setLayout(self.layout)

        self.layout.addWidget(self.progressBar)
        self.progressBar.setTextVisible(False)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(maxvalue)
        self.setStyleSheet(style.stylesheet)
        self.progressBar.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.processEvents()
    form = CPPNApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
