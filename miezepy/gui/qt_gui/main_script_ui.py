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
        script_widget.resize(1087, 716)
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
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_2 = QtWidgets.QFrame(self.process_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_17.addWidget(self.label_7)
        self.process_list_echo_times = QtWidgets.QListWidget(self.frame_2)
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
        self.verticalLayout_19.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_19.addWidget(self.label_9)
        self.process_list_selected = QtWidgets.QListView(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_list_selected.sizePolicy().hasHeightForWidth())
        self.process_list_selected.setSizePolicy(sizePolicy)
        self.process_list_selected.setObjectName("process_list_selected")
        self.verticalLayout_19.addWidget(self.process_list_selected)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_19.addWidget(self.label_10)
        self.time_channel_selected = QtWidgets.QListView(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_channel_selected.sizePolicy().hasHeightForWidth())
        self.time_channel_selected.setSizePolicy(sizePolicy)
        self.time_channel_selected.setObjectName("time_channel_selected")
        self.verticalLayout_19.addWidget(self.time_channel_selected)
        self.horizontalLayout_15.addLayout(self.verticalLayout_19)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_18.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_9.setContentsMargins(6, -1, 6, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.phase_mask_layout = QtWidgets.QVBoxLayout()
        self.phase_mask_layout.setContentsMargins(0, 0, -1, -1)
        self.phase_mask_layout.setSpacing(5)
        self.phase_mask_layout.setObjectName("phase_mask_layout")
        self.process_radio_mask = QtWidgets.QRadioButton(self.groupBox)
        self.process_radio_mask.setObjectName("process_radio_mask")
        self.phase_mask_layout.addWidget(self.process_radio_mask)
        self.verticalLayout_9.addLayout(self.phase_mask_layout)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.process_radio_exposure = QtWidgets.QRadioButton(self.groupBox)
        self.process_radio_exposure.setObjectName("process_radio_exposure")
        self.verticalLayout_12.addWidget(self.process_radio_exposure)
        self.process_box_instrument = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_box_instrument.sizePolicy().hasHeightForWidth())
        self.process_box_instrument.setSizePolicy(sizePolicy)
        self.process_box_instrument.setObjectName("process_box_instrument")
        self.verticalLayout_12.addWidget(self.process_box_instrument)
        self.process_box_detector = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_box_detector.sizePolicy().hasHeightForWidth())
        self.process_box_detector.setSizePolicy(sizePolicy)
        self.process_box_detector.setObjectName("process_box_detector")
        self.verticalLayout_12.addWidget(self.process_box_detector)
        self.verticalLayout_9.addLayout(self.verticalLayout_12)
        self.verticalLayout_18.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setContentsMargins(6, -1, 6, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.fit_select_layout = QtWidgets.QVBoxLayout()
        self.fit_select_layout.setContentsMargins(-1, -1, -1, 0)
        self.fit_select_layout.setSpacing(5)
        self.fit_select_layout.setObjectName("fit_select_layout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.fit_select_layout.addWidget(self.label_2)
        self.process_box_refs_fit = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_box_refs_fit.sizePolicy().hasHeightForWidth())
        self.process_box_refs_fit.setSizePolicy(sizePolicy)
        self.process_box_refs_fit.setObjectName("process_box_refs_fit")
        self.fit_select_layout.addWidget(self.process_box_refs_fit)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.fit_select_layout.addWidget(self.label_3)
        self.process_box_back_fit = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_box_back_fit.sizePolicy().hasHeightForWidth())
        self.process_box_back_fit.setSizePolicy(sizePolicy)
        self.process_box_back_fit.setObjectName("process_box_back_fit")
        self.fit_select_layout.addWidget(self.process_box_back_fit)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.fit_select_layout.addWidget(self.label_4)
        self.verticalLayout_10.addLayout(self.fit_select_layout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.verticalLayout_18.addWidget(self.groupBox_3)
        self.horizontalLayout_15.addLayout(self.verticalLayout_18)
        self.verticalLayout_7.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_12.addWidget(self.frame_2)
        self.verticalLayout_15.addLayout(self.horizontalLayout_12)
        self.frame_5 = QtWidgets.QFrame(self.process_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(5000, 5000))
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(0, -1, -1, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.process_button_run_data = QtWidgets.QPushButton(self.frame_5)
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
        self.horizontalLayout_2.addWidget(self.process_button_run_data)
        self.process_button_run_phase = QtWidgets.QPushButton(self.frame_5)
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
        self.horizontalLayout_2.addWidget(self.process_button_run_phase)
        self.process_button_run_fit = QtWidgets.QPushButton(self.frame_5)
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
        self.horizontalLayout_2.addWidget(self.process_button_run_fit)
        self.process_button_run_post = QtWidgets.QPushButton(self.frame_5)
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
        self.horizontalLayout_2.addWidget(self.process_button_run_post)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_14.addLayout(self.gridLayout_4)
        self.script_label_running = QtWidgets.QLabel(self.frame_5)
        self.script_label_running.setObjectName("script_label_running")
        self.horizontalLayout_14.addWidget(self.script_label_running)
        self.script_bar_running = QtWidgets.QProgressBar(self.frame_5)
        self.script_bar_running.setMinimumSize(QtCore.QSize(150, 0))
        self.script_bar_running.setMaximumSize(QtCore.QSize(150, 16777215))
        self.script_bar_running.setProperty("value", 24)
        self.script_bar_running.setObjectName("script_bar_running")
        self.horizontalLayout_14.addWidget(self.script_bar_running)
        self.scrip_label_action = QtWidgets.QLabel(self.frame_5)
        self.scrip_label_action.setObjectName("scrip_label_action")
        self.horizontalLayout_14.addWidget(self.scrip_label_action)
        self.script_label_action_2 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.script_label_action_2.sizePolicy().hasHeightForWidth())
        self.script_label_action_2.setSizePolicy(sizePolicy)
        self.script_label_action_2.setMinimumSize(QtCore.QSize(0, 0))
        self.script_label_action_2.setMaximumSize(QtCore.QSize(600, 16777215))
        self.script_label_action_2.setWordWrap(True)
        self.script_label_action_2.setObjectName("script_label_action_2")
        self.horizontalLayout_14.addWidget(self.script_label_action_2)
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_14)
        self.verticalLayout_15.addWidget(self.frame_5)
        self.horizontalLayout_13.addLayout(self.verticalLayout_15)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
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
        self.label_7.setText(_translate("script_widget", "Select the foils to consider for each echo time:"))
        self.label_9.setText(_translate("script_widget", "Selected measurements:"))
        self.label_10.setText(_translate("script_widget", "Selected time channels:"))
        self.groupBox.setTitle(_translate("script_widget", "Phase settings"))
        self.process_radio_mask.setText(_translate("script_widget", "Use mas&k method"))
        self.process_radio_exposure.setText(_translate("script_widget", "&Use high exposure"))
        self.process_box_instrument.setStatusTip(_translate("script_widget", "Select an Instrument"))
        self.process_box_detector.setStatusTip(_translate("script_widget", "Select a correction data"))
        self.groupBox_3.setTitle(_translate("script_widget", "Reduction settings"))
        self.label_2.setText(_translate("script_widget", "Reference measurement: "))
        self.label_3.setText(_translate("script_widget", "Background measurement:"))
        self.label_4.setText(_translate("script_widget", "Mask for reduction:"))
        self.process_button_run_data.setToolTip(_translate("script_widget", "Set metadata and fit parameters"))
        self.process_button_run_phase.setToolTip(_translate("script_widget", "Run phase processing script"))
        self.process_button_run_fit.setToolTip(_translate("script_widget", "Run Reduction script"))
        self.process_button_run_post.setToolTip(_translate("script_widget", "Run post-reduction script"))
        self.script_label_running.setText(_translate("script_widget", "Script running:"))
        self.scrip_label_action.setText(_translate("script_widget", "Action:"))
        self.script_label_action_2.setText(_translate("script_widget", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.process_tab), _translate("script_widget", "Process"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.panel_tab), _translate("script_widget", "Panel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.script_tab), _translate("script_widget", "Scripts"))

