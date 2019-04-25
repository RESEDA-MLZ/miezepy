# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_result.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_result_widget(object):
    def setupUi(self, result_widget):
        result_widget.setObjectName("result_widget")
        result_widget.resize(1247, 662)
        result_widget.setStyleSheet("#result_widget{background-color: rgb(179, 179, 179);}\n"
"QGroupBox::title{color:rgb(0, 0, 0)}\n"
"QLabel{color:rgb(0, 0, 0)}\n"
"QTabWidget{background-color: rgb(131, 131, 131);}\n"
"QCheckBox{color:rgb(0, 0, 0)}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(result_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(result_widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.data_group = QtWidgets.QGroupBox(self.splitter)
        self.data_group.setObjectName("data_group")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.data_group)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.data_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.result_tab = QtWidgets.QWidget()
        self.result_tab.setObjectName("result_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.result_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.process_list_results = QtWidgets.QListView(self.result_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_list_results.sizePolicy().hasHeightForWidth())
        self.process_list_results.setSizePolicy(sizePolicy)
        self.process_list_results.setMinimumSize(QtCore.QSize(250, 0))
        self.process_list_results.setMaximumSize(QtCore.QSize(250, 16777215))
        self.process_list_results.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.process_list_results.setProperty("showDropIndicator", False)
        self.process_list_results.setAlternatingRowColors(False)
        self.process_list_results.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.process_list_results.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.process_list_results.setObjectName("process_list_results")
        self.verticalLayout_3.addWidget(self.process_list_results)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.process_button_refresh = QtWidgets.QPushButton(self.result_tab)
        self.process_button_refresh.setObjectName("process_button_refresh")
        self.horizontalLayout.addWidget(self.process_button_refresh)
        self.process_button_set = QtWidgets.QPushButton(self.result_tab)
        self.process_button_set.setDefault(True)
        self.process_button_set.setObjectName("process_button_set")
        self.horizontalLayout.addWidget(self.process_button_set)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.result_tab, "")
        self.data_tab = QtWidgets.QWidget()
        self.data_tab.setObjectName("data_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.data_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.data_tab)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_10.addWidget(self.label_12)
        self.process_tree_x = QtWidgets.QTreeWidget(self.data_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_tree_x.sizePolicy().hasHeightForWidth())
        self.process_tree_x.setSizePolicy(sizePolicy)
        self.process_tree_x.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.process_tree_x.setProperty("showDropIndicator", False)
        self.process_tree_x.setAlternatingRowColors(False)
        self.process_tree_x.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.process_tree_x.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.process_tree_x.setAnimated(False)
        self.process_tree_x.setObjectName("process_tree_x")
        self.process_tree_x.headerItem().setText(0, "1")
        self.process_tree_x.header().setVisible(False)
        self.process_tree_x.header().setCascadingSectionResizes(False)
        self.process_tree_x.header().setHighlightSections(False)
        self.process_tree_x.header().setStretchLastSection(True)
        self.verticalLayout_10.addWidget(self.process_tree_x)
        self.label_10 = QtWidgets.QLabel(self.data_tab)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.process_tree_y = QtWidgets.QTreeWidget(self.data_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_tree_y.sizePolicy().hasHeightForWidth())
        self.process_tree_y.setSizePolicy(sizePolicy)
        self.process_tree_y.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.process_tree_y.setProperty("showDropIndicator", False)
        self.process_tree_y.setAlternatingRowColors(False)
        self.process_tree_y.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.process_tree_y.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.process_tree_y.setAnimated(False)
        self.process_tree_y.setObjectName("process_tree_y")
        self.process_tree_y.headerItem().setText(0, "1")
        self.process_tree_y.header().setVisible(False)
        self.process_tree_y.header().setCascadingSectionResizes(False)
        self.process_tree_y.header().setHighlightSections(False)
        self.process_tree_y.header().setStretchLastSection(True)
        self.verticalLayout_10.addWidget(self.process_tree_y)
        self.label_8 = QtWidgets.QLabel(self.data_tab)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.process_tree_error = QtWidgets.QTreeWidget(self.data_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_tree_error.sizePolicy().hasHeightForWidth())
        self.process_tree_error.setSizePolicy(sizePolicy)
        self.process_tree_error.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.process_tree_error.setProperty("showDropIndicator", False)
        self.process_tree_error.setAlternatingRowColors(False)
        self.process_tree_error.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.process_tree_error.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.process_tree_error.setAnimated(False)
        self.process_tree_error.setObjectName("process_tree_error")
        self.process_tree_error.headerItem().setText(0, "1")
        self.process_tree_error.header().setVisible(False)
        self.process_tree_error.header().setCascadingSectionResizes(False)
        self.process_tree_error.header().setHighlightSections(False)
        self.process_tree_error.header().setStretchLastSection(True)
        self.verticalLayout_10.addWidget(self.process_tree_error)
        self.verticalLayout_2.addLayout(self.verticalLayout_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.process_button_echo_fit = QtWidgets.QPushButton(self.data_tab)
        self.process_button_echo_fit.setObjectName("process_button_echo_fit")
        self.horizontalLayout_8.addWidget(self.process_button_echo_fit)
        self.process_button_gamma = QtWidgets.QPushButton(self.data_tab)
        self.process_button_gamma.setObjectName("process_button_gamma")
        self.horizontalLayout_8.addWidget(self.process_button_gamma)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.data_tab, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.process_widget_plot = QtWidgets.QWidget(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_widget_plot.sizePolicy().hasHeightForWidth())
        self.process_widget_plot.setSizePolicy(sizePolicy)
        self.process_widget_plot.setObjectName("process_widget_plot")
        self.verticalLayout_20.addWidget(self.process_widget_plot)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.process_check_offset = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_check_offset.sizePolicy().hasHeightForWidth())
        self.process_check_offset.setSizePolicy(sizePolicy)
        self.process_check_offset.setMinimumSize(QtCore.QSize(75, 0))
        self.process_check_offset.setMaximumSize(QtCore.QSize(75, 16777215))
        self.process_check_offset.setObjectName("process_check_offset")
        self.horizontalLayout_4.addWidget(self.process_check_offset)
        self.process_spin_offset = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_spin_offset.sizePolicy().hasHeightForWidth())
        self.process_spin_offset.setSizePolicy(sizePolicy)
        self.process_spin_offset.setMinimum(-100000000.0)
        self.process_spin_offset.setMaximum(100000000.0)
        self.process_spin_offset.setObjectName("process_spin_offset")
        self.horizontalLayout_4.addWidget(self.process_spin_offset)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(100, 0))
        self.label_11.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.process_spin_offset_total = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_spin_offset_total.sizePolicy().hasHeightForWidth())
        self.process_spin_offset_total.setSizePolicy(sizePolicy)
        self.process_spin_offset_total.setMinimum(-100000000.0)
        self.process_spin_offset_total.setMaximum(100000000.0)
        self.process_spin_offset_total.setObjectName("process_spin_offset_total")
        self.horizontalLayout_4.addWidget(self.process_spin_offset_total)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_20.addLayout(self.horizontalLayout_4)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.process_check_log_x = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_check_log_x.sizePolicy().hasHeightForWidth())
        self.process_check_log_x.setSizePolicy(sizePolicy)
        self.process_check_log_x.setMinimumSize(QtCore.QSize(75, 0))
        self.process_check_log_x.setMaximumSize(QtCore.QSize(75, 16777215))
        self.process_check_log_x.setObjectName("process_check_log_x")
        self.horizontalLayout_10.addWidget(self.process_check_log_x)
        self.process_check_log_y = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_check_log_y.sizePolicy().hasHeightForWidth())
        self.process_check_log_y.setSizePolicy(sizePolicy)
        self.process_check_log_y.setMinimumSize(QtCore.QSize(75, 0))
        self.process_check_log_y.setMaximumSize(QtCore.QSize(75, 16777215))
        self.process_check_log_y.setObjectName("process_check_log_y")
        self.horizontalLayout_10.addWidget(self.process_check_log_y)
        spacerItem1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.process_button_plot_plot = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_button_plot_plot.sizePolicy().hasHeightForWidth())
        self.process_button_plot_plot.setSizePolicy(sizePolicy)
        self.process_button_plot_plot.setDefault(True)
        self.process_button_plot_plot.setObjectName("process_button_plot_plot")
        self.horizontalLayout_10.addWidget(self.process_button_plot_plot)
        self.verticalLayout_21.addLayout(self.horizontalLayout_10)
        self.verticalLayout_20.addLayout(self.verticalLayout_21)
        self.plot_items_group = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_items_group.sizePolicy().hasHeightForWidth())
        self.plot_items_group.setSizePolicy(sizePolicy)
        self.plot_items_group.setMinimumSize(QtCore.QSize(400, 0))
        self.plot_items_group.setMaximumSize(QtCore.QSize(400, 16777215))
        self.plot_items_group.setObjectName("plot_items_group")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.plot_items_group)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.process_list_plot = QtWidgets.QListView(self.plot_items_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_list_plot.sizePolicy().hasHeightForWidth())
        self.process_list_plot.setSizePolicy(sizePolicy)
        self.process_list_plot.setMinimumSize(QtCore.QSize(0, 300))
        self.process_list_plot.setMaximumSize(QtCore.QSize(16777215, 300))
        self.process_list_plot.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.process_list_plot.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.process_list_plot.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.process_list_plot.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.process_list_plot.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.process_list_plot.setProperty("showDropIndicator", False)
        self.process_list_plot.setDragEnabled(False)
        self.process_list_plot.setAlternatingRowColors(True)
        self.process_list_plot.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.process_list_plot.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.process_list_plot.setObjectName("process_list_plot")
        self.verticalLayout_6.addWidget(self.process_list_plot)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.process_button_plot_add = QtWidgets.QPushButton(self.plot_items_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_button_plot_add.sizePolicy().hasHeightForWidth())
        self.process_button_plot_add.setSizePolicy(sizePolicy)
        self.process_button_plot_add.setObjectName("process_button_plot_add")
        self.horizontalLayout_9.addWidget(self.process_button_plot_add)
        self.process_button_plot_remove = QtWidgets.QPushButton(self.plot_items_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_button_plot_remove.sizePolicy().hasHeightForWidth())
        self.process_button_plot_remove.setSizePolicy(sizePolicy)
        self.process_button_plot_remove.setObjectName("process_button_plot_remove")
        self.horizontalLayout_9.addWidget(self.process_button_plot_remove)
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.process_button_plot_reset = QtWidgets.QPushButton(self.plot_items_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_button_plot_reset.sizePolicy().hasHeightForWidth())
        self.process_button_plot_reset.setSizePolicy(sizePolicy)
        self.process_button_plot_reset.setObjectName("process_button_plot_reset")
        self.horizontalLayout_9.addWidget(self.process_button_plot_reset)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.plot_items_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setAutoFillBackground(False)
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget_2.setUsesScrollButtons(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.Data = QtWidgets.QWidget()
        self.Data.setObjectName("Data")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Data)
        self.verticalLayout_7.setContentsMargins(6, 6, -1, 6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.x_input = QtWidgets.QComboBox(self.Data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_input.sizePolicy().hasHeightForWidth())
        self.x_input.setSizePolicy(sizePolicy)
        self.x_input.setObjectName("x_input")
        self.gridLayout.addWidget(self.x_input, 0, 1, 1, 1)
        self.error_label = QtWidgets.QLabel(self.Data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_label.sizePolicy().hasHeightForWidth())
        self.error_label.setSizePolicy(sizePolicy)
        self.error_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.error_label.setObjectName("error_label")
        self.gridLayout.addWidget(self.error_label, 2, 0, 1, 1)
        self.y_label = QtWidgets.QLabel(self.Data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_label.sizePolicy().hasHeightForWidth())
        self.y_label.setSizePolicy(sizePolicy)
        self.y_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.y_label.setObjectName("y_label")
        self.gridLayout.addWidget(self.y_label, 1, 0, 1, 1)
        self.y_input = QtWidgets.QComboBox(self.Data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_input.sizePolicy().hasHeightForWidth())
        self.y_input.setSizePolicy(sizePolicy)
        self.y_input.setObjectName("y_input")
        self.gridLayout.addWidget(self.y_input, 1, 1, 1, 1)
        self.x_label = QtWidgets.QLabel(self.Data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_label.sizePolicy().hasHeightForWidth())
        self.x_label.setSizePolicy(sizePolicy)
        self.x_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.x_label.setObjectName("x_label")
        self.gridLayout.addWidget(self.x_label, 0, 0, 1, 1)
        self.error_input = QtWidgets.QComboBox(self.Data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_input.sizePolicy().hasHeightForWidth())
        self.error_input.setSizePolicy(sizePolicy)
        self.error_input.setObjectName("error_input")
        self.gridLayout.addWidget(self.error_input, 2, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.process_table_data = QtWidgets.QTableView(self.Data)
        self.process_table_data.setObjectName("process_table_data")
        self.verticalLayout_7.addWidget(self.process_table_data)
        self.tabWidget_2.addTab(self.Data, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.offset_label = QtWidgets.QLabel(self.tab)
        self.offset_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.offset_label.setObjectName("offset_label")
        self.gridLayout_3.addWidget(self.offset_label, 1, 0, 1, 1)
        self.link_label = QtWidgets.QLabel(self.tab)
        self.link_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.link_label.setObjectName("link_label")
        self.gridLayout_3.addWidget(self.link_label, 2, 0, 1, 1)
        self.link_input = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.link_input.sizePolicy().hasHeightForWidth())
        self.link_input.setSizePolicy(sizePolicy)
        self.link_input.setObjectName("link_input")
        self.gridLayout_3.addWidget(self.link_input, 2, 1, 1, 1)
        self.active_check = QtWidgets.QCheckBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.active_check.sizePolicy().hasHeightForWidth())
        self.active_check.setSizePolicy(sizePolicy)
        self.active_check.setText("")
        self.active_check.setObjectName("active_check")
        self.gridLayout_3.addWidget(self.active_check, 0, 1, 1, 1)
        self.active_label = QtWidgets.QLabel(self.tab)
        self.active_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.active_label.setObjectName("active_label")
        self.gridLayout_3.addWidget(self.active_label, 0, 0, 1, 1)
        self.offset_spin = QtWidgets.QDoubleSpinBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offset_spin.sizePolicy().hasHeightForWidth())
        self.offset_spin.setSizePolicy(sizePolicy)
        self.offset_spin.setMinimum(-100000000.0)
        self.offset_spin.setMaximum(100000000.0)
        self.offset_spin.setObjectName("offset_spin")
        self.gridLayout_3.addWidget(self.offset_spin, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 3, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab, "")
        self.Plot = QtWidgets.QWidget()
        self.Plot.setObjectName("Plot")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Plot)
        self.gridLayout_2.setContentsMargins(-1, 6, -1, 6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_thickness_label = QtWidgets.QLabel(self.Plot)
        self.line_thickness_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_thickness_label.setObjectName("line_thickness_label")
        self.gridLayout_2.addWidget(self.line_thickness_label, 1, 3, 1, 1)
        self.color_button = QtWidgets.QPushButton(self.Plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_button.sizePolicy().hasHeightForWidth())
        self.color_button.setSizePolicy(sizePolicy)
        self.color_button.setStyleSheet("#color_button{\n"
"background-color: rgb(106, 106, 106);\n"
"border-style: inset;\n"
"border-width: 2px}\n"
"\n"
"#color_button:pressed{\n"
"border-style: outset;\n"
"border-width: 2px}\n"
"")
        self.color_button.setText("")
        self.color_button.setAutoDefault(False)
        self.color_button.setFlat(False)
        self.color_button.setObjectName("color_button")
        self.gridLayout_2.addWidget(self.color_button, 2, 2, 1, 1)
        self.scatter_size_label = QtWidgets.QLabel(self.Plot)
        self.scatter_size_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.scatter_size_label.setObjectName("scatter_size_label")
        self.gridLayout_2.addWidget(self.scatter_size_label, 0, 3, 1, 1)
        self.line_thickness_spin = QtWidgets.QSpinBox(self.Plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_thickness_spin.sizePolicy().hasHeightForWidth())
        self.line_thickness_spin.setSizePolicy(sizePolicy)
        self.line_thickness_spin.setObjectName("line_thickness_spin")
        self.gridLayout_2.addWidget(self.line_thickness_spin, 1, 4, 1, 1)
        self.scatter_type_combo = QtWidgets.QComboBox(self.Plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scatter_type_combo.sizePolicy().hasHeightForWidth())
        self.scatter_type_combo.setSizePolicy(sizePolicy)
        self.scatter_type_combo.setObjectName("scatter_type_combo")
        self.scatter_type_combo.addItem("")
        self.scatter_type_combo.addItem("")
        self.scatter_type_combo.addItem("")
        self.scatter_type_combo.addItem("")
        self.gridLayout_2.addWidget(self.scatter_type_combo, 0, 2, 1, 1)
        self.line_type_label_2 = QtWidgets.QLabel(self.Plot)
        self.line_type_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.line_type_label_2.setObjectName("line_type_label_2")
        self.gridLayout_2.addWidget(self.line_type_label_2, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 5, 1, 1)
        self.scatter_size_spin = QtWidgets.QSpinBox(self.Plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scatter_size_spin.sizePolicy().hasHeightForWidth())
        self.scatter_size_spin.setSizePolicy(sizePolicy)
        self.scatter_size_spin.setObjectName("scatter_size_spin")
        self.gridLayout_2.addWidget(self.scatter_size_spin, 0, 4, 1, 1)
        self.line_type_label = QtWidgets.QLabel(self.Plot)
        self.line_type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.line_type_label.setObjectName("line_type_label")
        self.gridLayout_2.addWidget(self.line_type_label, 1, 1, 1, 1)
        self.scatter_type_label = QtWidgets.QLabel(self.Plot)
        self.scatter_type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.scatter_type_label.setObjectName("scatter_type_label")
        self.gridLayout_2.addWidget(self.scatter_type_label, 0, 1, 1, 1)
        self.line_type_combo = QtWidgets.QComboBox(self.Plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_type_combo.sizePolicy().hasHeightForWidth())
        self.line_type_combo.setSizePolicy(sizePolicy)
        self.line_type_combo.setObjectName("line_type_combo")
        self.gridLayout_2.addWidget(self.line_type_combo, 1, 2, 1, 1)
        self.scatter_check = QtWidgets.QCheckBox(self.Plot)
        self.scatter_check.setObjectName("scatter_check")
        self.gridLayout_2.addWidget(self.scatter_check, 0, 0, 1, 1)
        self.line_check = QtWidgets.QCheckBox(self.Plot)
        self.line_check.setObjectName("line_check")
        self.gridLayout_2.addWidget(self.line_check, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 3, 2, 1, 1)
        self.tabWidget_2.addTab(self.Plot, "")
        self.verticalLayout_6.addWidget(self.tabWidget_2)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(result_widget)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(result_widget)

    def retranslateUi(self, result_widget):
        _translate = QtCore.QCoreApplication.translate
        result_widget.setWindowTitle(_translate("result_widget", "Form"))
        self.data_group.setTitle(_translate("result_widget", "Data"))
        self.process_button_refresh.setText(_translate("result_widget", "Refresh"))
        self.process_button_set.setText(_translate("result_widget", "Set"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.result_tab), _translate("result_widget", "Results"))
        self.label_12.setText(_translate("result_widget", "Select x"))
        self.process_tree_x.setSortingEnabled(True)
        self.label_10.setText(_translate("result_widget", "Select y"))
        self.process_tree_y.setSortingEnabled(True)
        self.label_8.setText(_translate("result_widget", "Select error"))
        self.process_tree_error.setSortingEnabled(True)
        self.process_button_echo_fit.setText(_translate("result_widget", "Echo Fit"))
        self.process_button_gamma.setText(_translate("result_widget", "Gamma"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data_tab), _translate("result_widget", "Data"))
        self.groupBox_3.setTitle(_translate("result_widget", "Plot"))
        self.process_check_offset.setText(_translate("result_widget", "Offset"))
        self.label_11.setText(_translate("result_widget", "x curve num +"))
        self.process_check_log_x.setText(_translate("result_widget", "Log x"))
        self.process_check_log_y.setText(_translate("result_widget", "Log y"))
        self.process_button_plot_plot.setText(_translate("result_widget", "Plot"))
        self.plot_items_group.setTitle(_translate("result_widget", "Plot Items"))
        self.process_button_plot_add.setText(_translate("result_widget", "+"))
        self.process_button_plot_remove.setText(_translate("result_widget", "-"))
        self.process_button_plot_reset.setText(_translate("result_widget", "Reset"))
        self.error_label.setText(_translate("result_widget", "error"))
        self.y_label.setText(_translate("result_widget", "y input"))
        self.x_label.setText(_translate("result_widget", "x input"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Data), _translate("result_widget", "Data"))
        self.offset_label.setText(_translate("result_widget", "offset"))
        self.link_label.setText(_translate("result_widget", "link"))
        self.active_label.setText(_translate("result_widget", "actif"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("result_widget", "Settings"))
        self.line_thickness_label.setText(_translate("result_widget", "Thickness"))
        self.scatter_size_label.setText(_translate("result_widget", "Size"))
        self.scatter_type_combo.setItemText(0, _translate("result_widget", "circle"))
        self.scatter_type_combo.setItemText(1, _translate("result_widget", "square"))
        self.scatter_type_combo.setItemText(2, _translate("result_widget", "triangle"))
        self.scatter_type_combo.setItemText(3, _translate("result_widget", "diamond"))
        self.line_type_label_2.setText(_translate("result_widget", "Color"))
        self.line_type_label.setText(_translate("result_widget", "Type"))
        self.scatter_type_label.setText(_translate("result_widget", "Type"))
        self.scatter_check.setText(_translate("result_widget", "Scatter Plot"))
        self.line_check.setText(_translate("result_widget", "Line Plot"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Plot), _translate("result_widget", "Visual"))

