# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_script.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_script_widget(object):
    def setupUi(self, script_widget):
        script_widget.setObjectName("script_widget")
        script_widget.resize(1571, 1316)
        script_widget.setStyleSheet("#script_widget{background-color: rgb(179, 179, 179);}\n"
"QGroupBox::title{color:rgb(0, 0, 0)}\n"
"QLabel{color:rgb(0, 0, 0)}\n"
"QTabWidget{background-color: rgb(131, 131, 131);}\n"
"#process_tab{background-color: rgb(131, 131, 131);}\n"
"#panel_tab{background-color: rgb(131, 131, 131);}\n"
"#script_tab{background-color: rgb(131, 131, 131);}\n"
"#script_tab_import{background-color: rgb(131, 131, 131);}\n"
"#script_tab_set_fit{background-color: rgb(131, 131, 131);}\n"
"#script_tab_phase{background-color: rgb(131, 131, 131);}\n"
"#script_tab_reduction{background-color: rgb(131, 131, 131);}\n"
"#tab{background-color: rgb(131, 131, 131);}")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(script_widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(script_widget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.process_tab = QtWidgets.QWidget()
        self.process_tab.setObjectName("process_tab")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.process_tab)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.groupBox_2 = QtWidgets.QGroupBox(self.process_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout_16.addWidget(self.label)
        self.horizontalLayout_4.addLayout(self.verticalLayout_16)
        self.process_layout_foil_check = QtWidgets.QHBoxLayout()
        self.process_layout_foil_check.setObjectName("process_layout_foil_check")
        self.horizontalLayout_4.addLayout(self.process_layout_foil_check)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setContentsMargins(0, 10, -1, -1)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_17.addWidget(self.label_7)
        self.process_list_echo_times = QtWidgets.QListWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_list_echo_times.sizePolicy().hasHeightForWidth())
        self.process_list_echo_times.setSizePolicy(sizePolicy)
        self.process_list_echo_times.setMinimumSize(QtCore.QSize(500, 0))
        self.process_list_echo_times.setMaximumSize(QtCore.QSize(500, 16777215))
        self.process_list_echo_times.setBaseSize(QtCore.QSize(500, 0))
        self.process_list_echo_times.setObjectName("process_list_echo_times")
        self.verticalLayout_17.addWidget(self.process_list_echo_times)
        self.horizontalLayout_15.addLayout(self.verticalLayout_17)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setContentsMargins(0, 10, -1, -1)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_19.addWidget(self.label_9)
        self.process_list_selected = QtWidgets.QListView(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_list_selected.sizePolicy().hasHeightForWidth())
        self.process_list_selected.setSizePolicy(sizePolicy)
        self.process_list_selected.setObjectName("process_list_selected")
        self.verticalLayout_19.addWidget(self.process_list_selected)
        self.horizontalLayout_15.addLayout(self.verticalLayout_19)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_18.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_9.setContentsMargins(6, -1, 6, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.process_radio_mask = QtWidgets.QRadioButton(self.groupBox)
        self.process_radio_mask.setObjectName("process_radio_mask")
        self.verticalLayout_13.addWidget(self.process_radio_mask)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_13.addWidget(self.label_6)
        self.process_box_masks = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_box_masks.sizePolicy().hasHeightForWidth())
        self.process_box_masks.setSizePolicy(sizePolicy)
        self.process_box_masks.setObjectName("process_box_masks")
        self.verticalLayout_13.addWidget(self.process_box_masks)
        self.verticalLayout_9.addLayout(self.verticalLayout_13)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.process_radio_exposure = QtWidgets.QRadioButton(self.groupBox)
        self.process_radio_exposure.setObjectName("process_radio_exposure")
        self.verticalLayout_12.addWidget(self.process_radio_exposure)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.label_5)
        self.process_box_refs = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_box_refs.sizePolicy().hasHeightForWidth())
        self.process_box_refs.setSizePolicy(sizePolicy)
        self.process_box_refs.setObjectName("process_box_refs")
        self.verticalLayout_12.addWidget(self.process_box_refs)
        self.verticalLayout_9.addLayout(self.verticalLayout_12)
        self.verticalLayout_18.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setContentsMargins(6, -1, 6, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_11.addWidget(self.label_2)
        self.process_box_refs_fit = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_box_refs_fit.sizePolicy().hasHeightForWidth())
        self.process_box_refs_fit.setSizePolicy(sizePolicy)
        self.process_box_refs_fit.setObjectName("process_box_refs_fit")
        self.verticalLayout_11.addWidget(self.process_box_refs_fit)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_11.addWidget(self.label_3)
        self.process_box_back_fit = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_box_back_fit.sizePolicy().hasHeightForWidth())
        self.process_box_back_fit.setSizePolicy(sizePolicy)
        self.process_box_back_fit.setObjectName("process_box_back_fit")
        self.verticalLayout_11.addWidget(self.process_box_back_fit)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_11.addWidget(self.label_4)
        self.process_box_mask_fit = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_box_mask_fit.sizePolicy().hasHeightForWidth())
        self.process_box_mask_fit.setSizePolicy(sizePolicy)
        self.process_box_mask_fit.setObjectName("process_box_mask_fit")
        self.verticalLayout_11.addWidget(self.process_box_mask_fit)
        self.verticalLayout_10.addLayout(self.verticalLayout_11)
        self.verticalLayout_18.addWidget(self.groupBox_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(220, 350))
        self.groupBox_4.setMaximumSize(QtCore.QSize(220, 350))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.process_button_run_data = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_button_run_data.sizePolicy().hasHeightForWidth())
        self.process_button_run_data.setSizePolicy(sizePolicy)
        self.process_button_run_data.setMinimumSize(QtCore.QSize(50, 50))
        self.process_button_run_data.setMaximumSize(QtCore.QSize(50, 50))
        self.process_button_run_data.setStyleSheet("#process_button_run_data { \n"
"background-color: transparent; \n"
"qproperty-icon: url(:/Ressources/run_data.ico); \n"
"background-color: rgba(213, 211, 214, 92);\n"
"border-style: inset;\n"
"border-width: 2px;\n"
"\n"
"} \n"
"#process_button_run_data:pressed { \n"
"border-style: outset;\n"
"}\n"
"\n"
"")
        self.process_button_run_data.setText("")
        self.process_button_run_data.setIconSize(QtCore.QSize(40, 40))
        self.process_button_run_data.setFlat(False)
        self.process_button_run_data.setObjectName("process_button_run_data")
        self.gridLayout_2.addWidget(self.process_button_run_data, 0, 0, 1, 1)
        self.process_button_run_fit = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_button_run_fit.sizePolicy().hasHeightForWidth())
        self.process_button_run_fit.setSizePolicy(sizePolicy)
        self.process_button_run_fit.setMinimumSize(QtCore.QSize(50, 50))
        self.process_button_run_fit.setMaximumSize(QtCore.QSize(50, 50))
        self.process_button_run_fit.setStyleSheet("#process_button_run_fit { \n"
"background-color: transparent; \n"
"qproperty-icon: url(:/Ressources/run_fit.ico); \n"
"background-color: rgba(213, 211, 214, 92);\n"
"border-style: inset;\n"
"border-width: 2px;\n"
"\n"
"} \n"
"#process_button_run_fit:pressed { \n"
"border-style: outset;\n"
"}\n"
"\n"
"")
        self.process_button_run_fit.setText("")
        self.process_button_run_fit.setIconSize(QtCore.QSize(40, 40))
        self.process_button_run_fit.setObjectName("process_button_run_fit")
        self.gridLayout_2.addWidget(self.process_button_run_fit, 2, 0, 1, 1)
        self.process_button_run_phase = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_button_run_phase.sizePolicy().hasHeightForWidth())
        self.process_button_run_phase.setSizePolicy(sizePolicy)
        self.process_button_run_phase.setMinimumSize(QtCore.QSize(50, 40))
        self.process_button_run_phase.setMaximumSize(QtCore.QSize(50, 50))
        self.process_button_run_phase.setStyleSheet("#process_button_run_phase { \n"
"background-color: transparent; \n"
"qproperty-icon: url(:/Ressources/run_phase.ico); \n"
"background-color: rgba(213, 211, 214, 92);\n"
"border-style: inset;\n"
"border-width: 2px;\n"
"\n"
"} \n"
"#process_button_run_phase:pressed { \n"
"border-style: outset;\n"
"}")
        self.process_button_run_phase.setText("")
        self.process_button_run_phase.setIconSize(QtCore.QSize(40, 40))
        self.process_button_run_phase.setObjectName("process_button_run_phase")
        self.gridLayout_2.addWidget(self.process_button_run_phase, 1, 0, 1, 1)
        self.process_button_run_post = QtWidgets.QPushButton(self.groupBox_4)
        self.process_button_run_post.setMinimumSize(QtCore.QSize(50, 50))
        self.process_button_run_post.setMaximumSize(QtCore.QSize(50, 50))
        self.process_button_run_post.setStyleSheet("#process_button_run_post { \n"
"background-color: transparent; \n"
"qproperty-icon: url(:/Ressources/run_post.ico); \n"
"background-color: rgba(213, 211, 214, 92);\n"
"border-style: inset;\n"
"border-width: 2px;\n"
"\n"
"} \n"
"#process_button_run_post:pressed { \n"
"border-style: outset;\n"
"}\n"
"")
        self.process_button_run_post.setText("")
        self.process_button_run_post.setIconSize(QtCore.QSize(40, 40))
        self.process_button_run_post.setObjectName("process_button_run_post")
        self.gridLayout_2.addWidget(self.process_button_run_post, 3, 0, 1, 1)
        self.horizontalLayout_11.addLayout(self.gridLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.progress_bar_reduction = QtWidgets.QProgressBar(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_bar_reduction.sizePolicy().hasHeightForWidth())
        self.progress_bar_reduction.setSizePolicy(sizePolicy)
        self.progress_bar_reduction.setProperty("value", 24)
        self.progress_bar_reduction.setOrientation(QtCore.Qt.Vertical)
        self.progress_bar_reduction.setInvertedAppearance(True)
        self.progress_bar_reduction.setObjectName("progress_bar_reduction")
        self.horizontalLayout_11.addWidget(self.progress_bar_reduction)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.process_button_script_data = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_button_script_data.sizePolicy().hasHeightForWidth())
        self.process_button_script_data.setSizePolicy(sizePolicy)
        self.process_button_script_data.setMinimumSize(QtCore.QSize(50, 50))
        self.process_button_script_data.setMaximumSize(QtCore.QSize(50, 50))
        self.process_button_script_data.setStyleSheet("#process_button_script_data { \n"
"background-color: transparent; \n"
"qproperty-icon: url(:/Ressources/script_data.ico); \n"
"background-color: rgba(213, 211, 214, 92);\n"
"border-style: inset;\n"
"border-width: 2px;\n"
"\n"
"} \n"
"#process_button_script_data:pressed { \n"
"border-style: outset;\n"
"}")
        self.process_button_script_data.setText("")
        self.process_button_script_data.setIconSize(QtCore.QSize(40, 40))
        self.process_button_script_data.setObjectName("process_button_script_data")
        self.gridLayout_3.addWidget(self.process_button_script_data, 0, 0, 1, 1)
        self.process_button_script_phase = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_button_script_phase.sizePolicy().hasHeightForWidth())
        self.process_button_script_phase.setSizePolicy(sizePolicy)
        self.process_button_script_phase.setMinimumSize(QtCore.QSize(50, 50))
        self.process_button_script_phase.setMaximumSize(QtCore.QSize(50, 50))
        self.process_button_script_phase.setStyleSheet("#process_button_script_phase { \n"
"background-color: transparent; \n"
"qproperty-icon: url(:/Ressources/script_phase.ico); \n"
"background-color: rgba(213, 211, 214, 92);\n"
"border-style: inset;\n"
"border-width: 2px;\n"
"\n"
"} \n"
"#process_button_script_phase:pressed { \n"
"border-style: outset;\n"
"}\n"
"")
        self.process_button_script_phase.setText("")
        self.process_button_script_phase.setIconSize(QtCore.QSize(40, 40))
        self.process_button_script_phase.setObjectName("process_button_script_phase")
        self.gridLayout_3.addWidget(self.process_button_script_phase, 1, 0, 1, 1)
        self.process_button_script_fit = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_button_script_fit.sizePolicy().hasHeightForWidth())
        self.process_button_script_fit.setSizePolicy(sizePolicy)
        self.process_button_script_fit.setMinimumSize(QtCore.QSize(50, 50))
        self.process_button_script_fit.setMaximumSize(QtCore.QSize(50, 50))
        self.process_button_script_fit.setStyleSheet("#process_button_script_fit { \n"
"background-color: transparent; \n"
"qproperty-icon: url(:/Ressources/script_fit.ico); \n"
"background-color: rgba(213, 211, 214, 92);\n"
"border-style: inset;\n"
"border-width: 2px;\n"
"\n"
"} \n"
"#process_button_script_fit:pressed { \n"
"border-style: outset;\n"
"}\n"
"\n"
"")
        self.process_button_script_fit.setText("")
        self.process_button_script_fit.setIconSize(QtCore.QSize(40, 40))
        self.process_button_script_fit.setObjectName("process_button_script_fit")
        self.gridLayout_3.addWidget(self.process_button_script_fit, 2, 0, 1, 1)
        self.process_button_script_post = QtWidgets.QPushButton(self.groupBox_4)
        self.process_button_script_post.setMinimumSize(QtCore.QSize(50, 50))
        self.process_button_script_post.setMaximumSize(QtCore.QSize(50, 50))
        self.process_button_script_post.setStyleSheet("#process_button_script_post { \n"
"background-color: transparent; \n"
"qproperty-icon: url(:/Ressources/script_post.ico); \n"
"background-color: rgba(213, 211, 214, 92);\n"
"border-style: inset;\n"
"border-width: 2px;\n"
"\n"
"} \n"
"#process_button_script_post:pressed { \n"
"border-style: outset;\n"
"}\n"
"")
        self.process_button_script_post.setText("")
        self.process_button_script_post.setIconSize(QtCore.QSize(40, 40))
        self.process_button_script_post.setObjectName("process_button_script_post")
        self.gridLayout_3.addWidget(self.process_button_script_post, 3, 0, 1, 1)
        self.horizontalLayout_11.addLayout(self.gridLayout_3)
        self.verticalLayout_14.addLayout(self.horizontalLayout_11)
        self.verticalLayout_18.addWidget(self.groupBox_4)
        self.horizontalLayout_15.addLayout(self.verticalLayout_18)
        self.verticalLayout_7.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_12.addWidget(self.groupBox_2)
        self.verticalLayout_15.addLayout(self.horizontalLayout_12)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.script_label_running = QtWidgets.QLabel(self.process_tab)
        self.script_label_running.setObjectName("script_label_running")
        self.horizontalLayout.addWidget(self.script_label_running)
        self.script_bar_running = QtWidgets.QProgressBar(self.process_tab)
        self.script_bar_running.setMinimumSize(QtCore.QSize(150, 0))
        self.script_bar_running.setMaximumSize(QtCore.QSize(150, 16777215))
        self.script_bar_running.setProperty("value", 24)
        self.script_bar_running.setObjectName("script_bar_running")
        self.horizontalLayout.addWidget(self.script_bar_running)
        self.scrip_label_action = QtWidgets.QLabel(self.process_tab)
        self.scrip_label_action.setObjectName("scrip_label_action")
        self.horizontalLayout.addWidget(self.scrip_label_action)
        self.script_label_action_2 = QtWidgets.QLabel(self.process_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.script_label_action_2.sizePolicy().hasHeightForWidth())
        self.script_label_action_2.setSizePolicy(sizePolicy)
        self.script_label_action_2.setMinimumSize(QtCore.QSize(0, 0))
        self.script_label_action_2.setMaximumSize(QtCore.QSize(600, 16777215))
        self.script_label_action_2.setObjectName("script_label_action_2")
        self.horizontalLayout.addWidget(self.script_label_action_2)
        spacerItem4 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_15.addLayout(self.horizontalLayout)
        self.horizontalLayout_13.addLayout(self.verticalLayout_15)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.tabWidget.addTab(self.process_tab, "")
        self.panel_tab = QtWidgets.QWidget()
        self.panel_tab.setObjectName("panel_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.panel_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.panel_layout = QtWidgets.QVBoxLayout()
        self.panel_layout.setSpacing(0)
        self.panel_layout.setObjectName("panel_layout")
        self.verticalLayout.addLayout(self.panel_layout)
        self.tabWidget.addTab(self.panel_tab, "")
        self.script_tab = QtWidgets.QWidget()
        self.script_tab.setObjectName("script_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.script_tab)
        self.verticalLayout_6.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_6.addLayout(self.verticalLayout_8)
        self.tabWidget.addTab(self.script_tab, "")
        self.verticalLayout_5.addWidget(self.tabWidget)

        self.retranslateUi(script_widget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(script_widget)

    def retranslateUi(self, script_widget):
        _translate = QtCore.QCoreApplication.translate
        script_widget.setWindowTitle(_translate("script_widget", "Form"))
        self.groupBox_2.setTitle(_translate("script_widget", "Fit parameters"))
        self.label.setText(_translate("script_widget", "Foils to be considerd: "))
        self.label_7.setText(_translate("script_widget", "Select the foils to consider for each echo time:"))
        self.label_9.setText(_translate("script_widget", "Selected measurements:"))
        self.groupBox.setTitle(_translate("script_widget", "Phase settings"))
        self.process_radio_mask.setText(_translate("script_widget", "Use mas&k method"))
        self.label_6.setText(_translate("script_widget", "Select a mask:"))
        self.process_radio_exposure.setText(_translate("script_widget", "&Use high exposure"))
        self.label_5.setText(_translate("script_widget", "Select the measurement:"))
        self.groupBox_3.setTitle(_translate("script_widget", "Reduction settings"))
        self.label_2.setText(_translate("script_widget", "Reference measurement: "))
        self.label_3.setText(_translate("script_widget", "Background measurement:"))
        self.label_4.setText(_translate("script_widget", "Mask for reduction:"))
        self.groupBox_4.setTitle(_translate("script_widget", "Process"))
        self.script_label_running.setText(_translate("script_widget", "Script running:"))
        self.scrip_label_action.setText(_translate("script_widget", "Action:"))
        self.script_label_action_2.setText(_translate("script_widget", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.process_tab), _translate("script_widget", "Process"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.panel_tab), _translate("script_widget", "Panel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.script_tab), _translate("script_widget", "Scripts"))

