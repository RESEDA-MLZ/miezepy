# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loaded_data.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dataset_widget(object):
    def setupUi(self, dataset_widget):
        dataset_widget.setObjectName("dataset_widget")
        dataset_widget.setEnabled(True)
        dataset_widget.resize(656, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dataset_widget.sizePolicy().hasHeightForWidth())
        dataset_widget.setSizePolicy(sizePolicy)
        dataset_widget.setMinimumSize(QtCore.QSize(656, 200))
        dataset_widget.setMaximumSize(QtCore.QSize(16777215, 200))
        dataset_widget.setWindowOpacity(-3.0)
        dataset_widget.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(dataset_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.para_label = QtWidgets.QLabel(dataset_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.para_label.sizePolicy().hasHeightForWidth())
        self.para_label.setSizePolicy(sizePolicy)
        self.para_label.setObjectName("para_label")
        self.verticalLayout.addWidget(self.para_label)
        self.para_input = QtWidgets.QLineEdit(dataset_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.para_input.sizePolicy().hasHeightForWidth())
        self.para_input.setSizePolicy(sizePolicy)
        self.para_input.setObjectName("para_input")
        self.verticalLayout.addWidget(self.para_input)
        self.meas_label = QtWidgets.QLabel(dataset_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.meas_label.sizePolicy().hasHeightForWidth())
        self.meas_label.setSizePolicy(sizePolicy)
        self.meas_label.setObjectName("meas_label")
        self.verticalLayout.addWidget(self.meas_label)
        self.meas_input = QtWidgets.QSpinBox(dataset_widget)
        self.meas_input.setObjectName("meas_input")
        self.verticalLayout.addWidget(self.meas_input)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ref_radio = QtWidgets.QCheckBox(dataset_widget)
        self.ref_radio.setObjectName("ref_radio")
        self.verticalLayout.addWidget(self.ref_radio)
        self.back_radio = QtWidgets.QCheckBox(dataset_widget)
        self.back_radio.setObjectName("back_radio")
        self.verticalLayout.addWidget(self.back_radio)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.vis_button = QtWidgets.QPushButton(dataset_widget)
        self.vis_button.setObjectName("vis_button")
        self.verticalLayout.addWidget(self.vis_button)
        self.vis_button_2 = QtWidgets.QPushButton(dataset_widget)
        self.vis_button_2.setObjectName("vis_button_2")
        self.verticalLayout.addWidget(self.vis_button_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.meta_table = QtWidgets.QTableView(dataset_widget)
        self.meta_table.setObjectName("meta_table")
        self.horizontalLayout.addWidget(self.meta_table)

        self.retranslateUi(dataset_widget)
        QtCore.QMetaObject.connectSlotsByName(dataset_widget)

    def retranslateUi(self, dataset_widget):
        _translate = QtCore.QCoreApplication.translate
        dataset_widget.setWindowTitle(_translate("dataset_widget", "dataset"))
        self.para_label.setText(_translate("dataset_widget", "Parameter:"))
        self.para_input.setToolTip(_translate("dataset_widget", "Parameter value such as temperature"))
        self.meas_label.setText(_translate("dataset_widget", "Measurement:"))
        self.ref_radio.setToolTip(_translate("dataset_widget", "Set the current element as reference"))
        self.ref_radio.setText(_translate("dataset_widget", "Reference"))
        self.back_radio.setToolTip(_translate("dataset_widget", "Set the current element as Background"))
        self.back_radio.setText(_translate("dataset_widget", "Background"))
        self.vis_button.setToolTip(_translate("dataset_widget", "Visualize the current element (Echo can be computed)"))
        self.vis_button.setText(_translate("dataset_widget", "Visualize"))
        self.vis_button_2.setToolTip(_translate("dataset_widget", "Visualize the current element (Echo can be computed)"))
        self.vis_button_2.setText(_translate("dataset_widget", "Visualize 4D"))


