# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_result.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui_result_widget(object):
    def setupUi(self, result_widget):
        result_widget.setObjectName("result_widget")
        result_widget.resize(1136, 662)
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
        # left
        self.data_group = QtWidgets.QGroupBox(self.splitter)
        self.data_group.setObjectName("data_group")
        self.data_group.setMinimumWidth(400)
        self.data_group.setStyleSheet("QGroupBox { background-color: white; border: 0;}")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.data_group)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        #
        self.scroll_widget = QtWidgets.QWidget() 
        self.scroll_widget.setStyleSheet("background-color: white;")
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.setSpacing(0)
        #self.scroll_widget.setMinimumWidth(300)  # Set a larger minimum width
        self.scroll_widget.setSizePolicy(QtWidgets.QScrollArea().sizePolicy())  # Allow it to expand if needed
        #
        self.dataselect_group = QtWidgets.QGroupBox(self.data_group)
        self.dataselect_group.setStyleSheet("QGroupBox { background-color: white; border: 0;}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataselect_group.sizePolicy().hasHeightForWidth())
        self.dataselect_group.setSizePolicy(sizePolicy)
        
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.dataselect_group)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        
        self.verticalLayout_411_label = QtWidgets.QVBoxLayout()
        self.verticalLayout_411_label.setObjectName("verticalLayout_411_label")
        self.data_label = QtWidgets.QLabel("Datasets:")
        self.data_label.setStyleSheet("font-weight: bold;")
        self.verticalLayout_411_label.addWidget(self.data_label)
        self.verticalLayout_411 = QtWidgets.QVBoxLayout()
        self.verticalLayout_411.setObjectName("verticalLayout_411")
        self.verticalLayout_411_label.addLayout(self.verticalLayout_411)
        self.verticalLayout_41.addLayout(self.verticalLayout_411_label)
        #
        self.verticalLayout_412 = QtWidgets.QVBoxLayout()
        self.verticalLayout_412.setObjectName("verticalLayout_412")
        spacer_vert11 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_412.addItem(spacer_vert11)
        self.verticalLayout_41.addLayout(self.verticalLayout_412)
        self.scroll_layout.addWidget(self.dataselect_group)
        
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_widget)
        self.verticalLayout_4.addWidget(self.scroll_area)   
        #
        self.verticalLayout_431 = QtWidgets.QVBoxLayout()
        self.process_refresh_button = QtWidgets.QPushButton('Refresh datasets', self.data_group)
        self.process_refresh_button.setObjectName("process_refresh_button")
        self.process_refresh_button.setDefault(True)
        self.verticalLayout_431.addWidget(self.process_refresh_button)
        self.verticalLayout_4.addLayout(self.verticalLayout_431)
        #
        spacer_vert_item = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacer_vert_item)
        #
        self.itemselect_group = QtWidgets.QGroupBox(self.data_group)
        self.itemselect_group.setStyleSheet("QGroupBox { background-color: white; border: 0; }")
        self.itemselect_group.setSizePolicy(sizePolicy)

        self.verticalLayout_61 = QtWidgets.QVBoxLayout()
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.itemselect_group.setLayout(self.verticalLayout_61)
        # functions for fitting
        self.fit_label = QtWidgets.QLabel("Fit functions:")
        self.fit_label.setStyleSheet("font-weight: bold;")
        self.verticalLayout_61.addWidget(self.fit_label)
        self.func1 = QtWidgets.QCheckBox(self.itemselect_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.func1.sizePolicy().hasHeightForWidth())
        self.func1.setSizePolicy(sizePolicy)
        self.func1.setMinimumSize(QtCore.QSize(75, 0))
        self.func1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.func1.setObjectName("func1")
        self.verticalLayout_61.addWidget(self.func1)
        self.func2 = QtWidgets.QCheckBox(self.itemselect_group)
        sizePolicy.setHeightForWidth(self.func2.sizePolicy().hasHeightForWidth())
        self.func2.setSizePolicy(sizePolicy)
        self.func2.setMinimumSize(QtCore.QSize(75, 0))
        self.func2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.func2.setObjectName("func2")
        self.verticalLayout_61.addWidget(self.func2)
        self.func3 = QtWidgets.QCheckBox(self.itemselect_group)
        sizePolicy.setHeightForWidth(self.func3.sizePolicy().hasHeightForWidth())
        self.func3.setSizePolicy(sizePolicy)
        self.func3.setMinimumSize(QtCore.QSize(75, 0))
        self.func3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.func3.setObjectName("func3")
        self.verticalLayout_61.addWidget(self.func3)
        self.func4 = QtWidgets.QCheckBox(self.itemselect_group)
        sizePolicy.setHeightForWidth(self.func4.sizePolicy().hasHeightForWidth())
        self.func4.setSizePolicy(sizePolicy)
        self.func4.setMinimumSize(QtCore.QSize(75, 0))
        self.func4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.func4.setObjectName("func4")
        self.verticalLayout_61.addWidget(self.func4)
        spacer_vert_func = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_61.addItem(spacer_vert_func)
        self.funcA = QtWidgets.QCheckBox(self.itemselect_group)
        sizePolicy.setHeightForWidth(self.funcA.sizePolicy().hasHeightForWidth())
        self.funcA.setSizePolicy(sizePolicy)
        self.funcA.setMinimumSize(QtCore.QSize(75, 0))
        self.funcA.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.funcA.setObjectName("funcA")
        self.verticalLayout_61.addWidget(self.funcA)
       
        self.verticalLayout_4.addWidget(self.itemselect_group)
        #
        self.verticalLayout_43 = QtWidgets.QVBoxLayout()
        self.plotitems_button = QtWidgets.QPushButton(self.data_group)
        self.plotitems_button.setDefault(True)
        self.plotitems_button.setObjectName("plotitems_button")
        self.verticalLayout_43.addWidget(self.plotitems_button)
        self.verticalLayout_4.addLayout(self.verticalLayout_43)
        #
        # right
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_3.setStyleSheet("QGroupBox {  border: 0; }")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        margins = self.verticalLayout_20.contentsMargins()
        self.verticalLayout_20.setContentsMargins(margins.left(), 0, margins.right(), margins.bottom())
        # the plot
        self.plot_widget = pg.PlotWidget()
        #self.plot_widget.setTitle("Plot title", color='black',size='14pt')
        self.plot_widget.getAxis('bottom').setPen(pg.mkPen(color='black', width=2))  
        self.plot_widget.getAxis('left').setPen(pg.mkPen(color='black', width=2))  
        self.plot_widget.getAxis('top').setPen(pg.mkPen(color='black', width=2))  
        self.plot_widget.getAxis('right').setPen(pg.mkPen(color='black', width=2))         
        self.plot_widget.getAxis('bottom').setTextPen(pg.mkPen(color='black'))  
        self.plot_widget.getAxis('left').setTextPen(pg.mkPen(color='black'))  
        self.plot_widget.getAxis('top').setStyle(showValues=False)
        self.plot_widget.getAxis('right').setStyle(showValues=False)
        self.plot_widget.showAxis('top')
        self.plot_widget.showAxis('right')
        self.plot_widget.setLogMode(x=False, y=False)
        self.plot_widget.setBackground('w')
        plot_item = self.plot_widget.getPlotItem()
        plot_item.setContentsMargins(20, 60, 60, 20) # left, top, right, bottom
        plot_item.getAxis('left').setLabel(text='Contrast (a.u.)',**{'color': 'black', 'font-size': '12pt'})
        plot_item.getAxis('bottom').setLabel(text='Echo time (ns)',**{'color': 'black', 'font-size': '12pt'})

        self.v_line = pg.InfiniteLine(angle=90, movable=False, pen=pg.mkPen(color = 'black', width=1))
        self.h_line = pg.InfiniteLine(angle=0, movable=False, pen=pg.mkPen(color = 'black', width=1))

        self.verticalLayout_20.addWidget(self.plot_widget)

        self.xy_label = QtWidgets.QLabel("")
        self.xy_label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_20.addWidget(self.xy_label)
        #
        #
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem5 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        #
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        # Errorbars checkbox
        self.add_errorbars = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_errorbars.sizePolicy().hasHeightForWidth())
        self.add_errorbars.setSizePolicy(sizePolicy)
        self.add_errorbars.setMinimumSize(QtCore.QSize(75, 0))
        self.add_errorbars.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.add_errorbars.setObjectName("add_errorbars")
        self.verticalLayout_10.addWidget(self.add_errorbars)
        #spacerItem20 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        #self.verticalLayout_10.addItem(spacerItem20)
        # Log X checkbox
        self.process_check_log_x = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_check_log_x.sizePolicy().hasHeightForWidth())
        self.process_check_log_x.setSizePolicy(sizePolicy)
        self.process_check_log_x.setMinimumSize(QtCore.QSize(75, 0))
        self.process_check_log_x.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.process_check_log_x.setObjectName("process_check_log_x")
        self.verticalLayout_10.addWidget(self.process_check_log_x)
        #spacerItem2 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        #self.verticalLayout_10.addItem(spacerItem2)
        # Log Y checkbox
        self.process_check_log_y = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_check_log_y.sizePolicy().hasHeightForWidth())
        self.process_check_log_y.setSizePolicy(sizePolicy)
        self.process_check_log_y.setMinimumSize(QtCore.QSize(75, 0))
        self.process_check_log_y.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.process_check_log_y.setObjectName("process_check_log_y")
        self.verticalLayout_10.addWidget(self.process_check_log_y)
        #spacerItem21 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        #self.verticalLayout_10.addItem(spacerItem21)
        self.horizontalLayout_10.addLayout(self.verticalLayout_10)
        #
        spacerItem4 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        #
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        # Crosshairs checkboxe
        self.process_check_crosshairs = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_check_crosshairs.sizePolicy().hasHeightForWidth())
        self.process_check_crosshairs.setSizePolicy(sizePolicy)
        self.process_check_crosshairs.setMinimumSize(QtCore.QSize(75, 0))
        self.process_check_crosshairs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.process_check_crosshairs.setObjectName("process_check_crosshairs")
        self.verticalLayout_11.addWidget(self.process_check_crosshairs)
        # Grid X checkbox
        self.process_check_grid_x = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_check_grid_x.sizePolicy().hasHeightForWidth())
        self.process_check_grid_x.setSizePolicy(sizePolicy)
        self.process_check_grid_x.setMinimumSize(QtCore.QSize(75, 0))
        self.process_check_grid_x.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.process_check_grid_x.setObjectName("process_check_grid_x")
        self.verticalLayout_11.addWidget(self.process_check_grid_x)
        #spacerItem22 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        #self.verticalLayout_11.addItem(spacerItem22)
        # Grid Y checkbox
        self.process_check_grid_y = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_check_grid_y.sizePolicy().hasHeightForWidth())
        self.process_check_grid_y.setSizePolicy(sizePolicy)
        self.process_check_grid_y.setMinimumSize(QtCore.QSize(75, 0))
        self.process_check_grid_y.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.process_check_grid_y.setObjectName("process_check_grid_y")
        self.verticalLayout_11.addWidget(self.process_check_grid_y)
        #spacerItem23 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        #self.verticalLayout_11.addItem(spacerItem23)
        self.horizontalLayout_10.addLayout(self.verticalLayout_11)
        spacerItem3 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        #
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        spacerItem6 = QtWidgets.QSpacerItem(10, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_12.addItem(spacerItem6)
        self.save_button = QtWidgets.QPushButton(self.data_group)
        self.save_button.setDefault(True)
        self.save_button.setObjectName("save_button")
        self.verticalLayout_12.addWidget(self.save_button)
        self.horizontalLayout_10.addItem(self.verticalLayout_12)
        #
        self.verticalLayout_20.addLayout(self.horizontalLayout_10)
        #
        #
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(result_widget)
        QtCore.QMetaObject.connectSlotsByName(result_widget)

    def retranslateUi(self, result_widget):
        _translate = QtCore.QCoreApplication.translate
        result_widget.setWindowTitle(_translate("result_widget", "Form"))
        #'''
        self.plotitems_button.setText(_translate("result_widget", "Plot"))
        self.save_button.setText(_translate("result_widget", "Save plot"))
        self.add_errorbars.setText(_translate("result_widget", "Error bars"))
        self.func1.setText(_translate("result_widget", "Exp. "))
        self.func1.setToolTip(  "<div style='white-space: nowrap;'>"
                                "Simple exponential decay <br>"
                                " I(q, &tau;) = A exp(- &Gamma; &tau; / ℏ)"
                                "</div>")
        self.func2.setText(_translate("result_widget", "Stretched exp. "))
        self.func2.setToolTip(  "<div style='white-space: nowrap;'>"
                                "Stretched exponential decay <br>"
                                " I(q, &tau;) = A exp(- &Gamma; &tau; / ℏ)<sup>&beta;</sup>"
                                "</div>")
        self.func3.setText(_translate("result_widget", "Str. exp. +El. BGRD"))
        self.func3.setToolTip(  "<div style='white-space: nowrap;'>"
                                "Stretched exponential decay with elastic component (background)<br>"
                                " I(q, &tau;) = A + (1 - A) exp(- &Gamma; &tau; / ℏ)<sup>&beta;</sup>"
                                "</div>")
        self.func4.setText(_translate("result_widget", "Str. exp. +INS"))
        self.func4.setToolTip(  "<div style='white-space: nowrap;'>"
                                "Stretched exponential decay with small inelastic contribution<br>"
                                " I(q, &tau;) = A exp(- &Gamma; &tau; / ℏ)<sup>&beta;</sup> cos(E &tau; / ℏ)"
                                "</div>") 
        self.funcA.setText(_translate("result_widget", "Fix fit param. A = 1"))
        self.funcA.setToolTip(  "<div style='white-space: nowrap;'>"
                                "Check the checkbox to fix the fitting parameter A = 1 <br>"
                                "for the Exponential, Stretched exponential and <br>" 
                                "Stretched exponential decay with inelastic contribution. <br>"
                                "<br>"
                                "Uncheck the checkbox to free this parameter."
                                "</div>") 
        self.process_check_log_x.setText(_translate("result_widget", "Set Log X"))
        self.process_check_log_y.setText(_translate("result_widget", "Set Log Y"))
        self.process_check_grid_x.setText(_translate("result_widget", "Set Grid X"))
        self.process_check_grid_y.setText(_translate("result_widget", "Set Grid Y"))
        self.process_check_crosshairs.setText(_translate("result_widget", "Set Crosshairs"))
        #'''


