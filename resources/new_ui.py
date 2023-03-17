# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AN_Chess(object):
    def setupUi(self, AN_Chess):
        AN_Chess.setObjectName("AN_Chess")
        AN_Chess.resize(744, 680)
        AN_Chess.setMinimumSize(QtCore.QSize(744, 680))
        AN_Chess.setMaximumSize(QtCore.QSize(744, 680))
        self.widget_board = QtWidgets.QWidget(AN_Chess)
        self.widget_board.setGeometry(QtCore.QRect(20, 20, 320, 320))
        self.widget_board.setMinimumSize(QtCore.QSize(320, 320))
        self.widget_board.setMaximumSize(QtCore.QSize(320, 320))
        self.widget_board.setStyleSheet("QWidget{\n"
"background-color: rgb(0, 127, 127);\n"
"color: rgb(0, 0, 0);\n"
"font: 28pt \"DFYeaSong-B5\";\n"
"}\n"
"\n"
"QPushButton[color=\"Red\"]{background-color: rgb(200, 0, 0);}\n"
"QPushButton[color=\"Blue\"]{background-color: rgb(0, 0, 200);}\n"
"\n"
"QPushButton[type=\"From\"][color=\"Red\"]{background-color: rgb(125, 0, 0)}\n"
"QPushButton[type=\"From\"][color=\"Blue\"]{background-color: rgb(0, 0, 125);}\n"
"\n"
"QPushButton[type=\"CanTo\"]{background-color: rgb(0, 180, 180)}\n"
"QPushButton[type=\"CanTo\"][color=\"Blue\"]{background-color: rgb(1, 114, 200)}\n"
"QPushButton[type=\"CanTo\"][color=\"Red\"]{background-color: rgb(200, 97, 97)}\n"
"")
        self.widget_board.setObjectName("widget_board")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_board)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.piece_20 = QtWidgets.QPushButton(self.widget_board)
        self.piece_20.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_20.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_20.setText("")
        self.piece_20.setProperty("type", "")
        self.piece_20.setObjectName("piece_20")
        self.gridLayout.addWidget(self.piece_20, 2, 0, 1, 1)
        self.piece_24 = QtWidgets.QPushButton(self.widget_board)
        self.piece_24.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_24.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_24.setStyleSheet("")
        self.piece_24.setText("")
        self.piece_24.setProperty("type", "")
        self.piece_24.setObjectName("piece_24")
        self.gridLayout.addWidget(self.piece_24, 2, 4, 1, 1)
        self.piece_03 = QtWidgets.QPushButton(self.widget_board)
        self.piece_03.setEnabled(False)
        self.piece_03.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_03.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_03.setText("")
        self.piece_03.setCheckable(False)
        self.piece_03.setProperty("type", "")
        self.piece_03.setProperty("color", "")
        self.piece_03.setObjectName("piece_03")
        self.gridLayout.addWidget(self.piece_03, 0, 3, 1, 1)
        self.piece_02 = QtWidgets.QPushButton(self.widget_board)
        self.piece_02.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_02.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_02.setText("")
        self.piece_02.setProperty("type", "")
        self.piece_02.setObjectName("piece_02")
        self.gridLayout.addWidget(self.piece_02, 0, 2, 1, 1)
        self.piece_01 = QtWidgets.QPushButton(self.widget_board)
        self.piece_01.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_01.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_01.setStyleSheet("")
        self.piece_01.setText("")
        self.piece_01.setProperty("type", "")
        self.piece_01.setObjectName("piece_01")
        self.gridLayout.addWidget(self.piece_01, 0, 1, 1, 1)
        self.piece_34 = QtWidgets.QPushButton(self.widget_board)
        self.piece_34.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_34.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_34.setStyleSheet("")
        self.piece_34.setText("")
        self.piece_34.setProperty("type", "")
        self.piece_34.setObjectName("piece_34")
        self.gridLayout.addWidget(self.piece_34, 3, 4, 1, 1)
        self.piece_42 = QtWidgets.QPushButton(self.widget_board)
        self.piece_42.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_42.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_42.setStyleSheet("")
        self.piece_42.setText("")
        self.piece_42.setProperty("type", "")
        self.piece_42.setObjectName("piece_42")
        self.gridLayout.addWidget(self.piece_42, 4, 2, 1, 1)
        self.piece_10 = QtWidgets.QPushButton(self.widget_board)
        self.piece_10.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_10.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_10.setText("")
        self.piece_10.setProperty("type", "")
        self.piece_10.setObjectName("piece_10")
        self.gridLayout.addWidget(self.piece_10, 1, 0, 1, 1)
        self.piece_13 = QtWidgets.QPushButton(self.widget_board)
        self.piece_13.setEnabled(False)
        self.piece_13.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_13.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_13.setText("")
        self.piece_13.setCheckable(False)
        self.piece_13.setProperty("type", "")
        self.piece_13.setProperty("color", "")
        self.piece_13.setObjectName("piece_13")
        self.gridLayout.addWidget(self.piece_13, 1, 3, 1, 1)
        self.piece_21 = QtWidgets.QPushButton(self.widget_board)
        self.piece_21.setEnabled(False)
        self.piece_21.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_21.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_21.setText("")
        self.piece_21.setCheckable(False)
        self.piece_21.setProperty("type", "")
        self.piece_21.setProperty("color", "")
        self.piece_21.setObjectName("piece_21")
        self.gridLayout.addWidget(self.piece_21, 2, 1, 1, 1)
        self.piece_32 = QtWidgets.QPushButton(self.widget_board)
        self.piece_32.setEnabled(False)
        self.piece_32.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_32.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_32.setText("")
        self.piece_32.setCheckable(False)
        self.piece_32.setProperty("type", "")
        self.piece_32.setProperty("color", "")
        self.piece_32.setObjectName("piece_32")
        self.gridLayout.addWidget(self.piece_32, 3, 2, 1, 1)
        self.piece_31 = QtWidgets.QPushButton(self.widget_board)
        self.piece_31.setEnabled(False)
        self.piece_31.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_31.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_31.setText("")
        self.piece_31.setCheckable(False)
        self.piece_31.setProperty("type", "")
        self.piece_31.setProperty("color", "")
        self.piece_31.setObjectName("piece_31")
        self.gridLayout.addWidget(self.piece_31, 3, 1, 1, 1)
        self.piece_44 = QtWidgets.QPushButton(self.widget_board)
        self.piece_44.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_44.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_44.setStyleSheet("")
        self.piece_44.setText("")
        self.piece_44.setProperty("type", "")
        self.piece_44.setObjectName("piece_44")
        self.gridLayout.addWidget(self.piece_44, 4, 4, 1, 1)
        self.piece_41 = QtWidgets.QPushButton(self.widget_board)
        self.piece_41.setEnabled(False)
        self.piece_41.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_41.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_41.setText("")
        self.piece_41.setCheckable(False)
        self.piece_41.setProperty("type", "")
        self.piece_41.setProperty("color", "")
        self.piece_41.setObjectName("piece_41")
        self.gridLayout.addWidget(self.piece_41, 4, 1, 1, 1)
        self.piece_33 = QtWidgets.QPushButton(self.widget_board)
        self.piece_33.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_33.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_33.setText("")
        self.piece_33.setProperty("type", "")
        self.piece_33.setObjectName("piece_33")
        self.gridLayout.addWidget(self.piece_33, 3, 3, 1, 1)
        self.piece_30 = QtWidgets.QPushButton(self.widget_board)
        self.piece_30.setEnabled(False)
        self.piece_30.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_30.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_30.setText("")
        self.piece_30.setCheckable(False)
        self.piece_30.setProperty("type", "")
        self.piece_30.setProperty("color", "")
        self.piece_30.setObjectName("piece_30")
        self.gridLayout.addWidget(self.piece_30, 3, 0, 1, 1)
        self.piece_04 = QtWidgets.QPushButton(self.widget_board)
        self.piece_04.setEnabled(False)
        self.piece_04.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_04.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_04.setText("")
        self.piece_04.setCheckable(False)
        self.piece_04.setProperty("type", "")
        self.piece_04.setProperty("color", "")
        self.piece_04.setObjectName("piece_04")
        self.gridLayout.addWidget(self.piece_04, 0, 4, 1, 1)
        self.piece_22 = QtWidgets.QPushButton(self.widget_board)
        self.piece_22.setEnabled(False)
        self.piece_22.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_22.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_22.setText("")
        self.piece_22.setCheckable(False)
        self.piece_22.setProperty("type", "")
        self.piece_22.setProperty("color", "")
        self.piece_22.setObjectName("piece_22")
        self.gridLayout.addWidget(self.piece_22, 2, 2, 1, 1)
        self.piece_23 = QtWidgets.QPushButton(self.widget_board)
        self.piece_23.setEnabled(False)
        self.piece_23.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_23.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_23.setStyleSheet("")
        self.piece_23.setText("")
        self.piece_23.setCheckable(False)
        self.piece_23.setProperty("type", "")
        self.piece_23.setProperty("color", "")
        self.piece_23.setObjectName("piece_23")
        self.gridLayout.addWidget(self.piece_23, 2, 3, 1, 1)
        self.piece_43 = QtWidgets.QPushButton(self.widget_board)
        self.piece_43.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_43.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_43.setText("")
        self.piece_43.setProperty("type", "")
        self.piece_43.setObjectName("piece_43")
        self.gridLayout.addWidget(self.piece_43, 4, 3, 1, 1)
        self.piece_14 = QtWidgets.QPushButton(self.widget_board)
        self.piece_14.setEnabled(False)
        self.piece_14.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_14.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_14.setText("")
        self.piece_14.setCheckable(False)
        self.piece_14.setProperty("type", "")
        self.piece_14.setProperty("color", "")
        self.piece_14.setObjectName("piece_14")
        self.gridLayout.addWidget(self.piece_14, 1, 4, 1, 1)
        self.piece_12 = QtWidgets.QPushButton(self.widget_board)
        self.piece_12.setEnabled(False)
        self.piece_12.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_12.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_12.setText("")
        self.piece_12.setCheckable(False)
        self.piece_12.setProperty("type", "")
        self.piece_12.setProperty("color", "")
        self.piece_12.setObjectName("piece_12")
        self.gridLayout.addWidget(self.piece_12, 1, 2, 1, 1)
        self.piece_11 = QtWidgets.QPushButton(self.widget_board)
        self.piece_11.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_11.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_11.setText("")
        self.piece_11.setProperty("type", "")
        self.piece_11.setObjectName("piece_11")
        self.gridLayout.addWidget(self.piece_11, 1, 1, 1, 1)
        self.piece_40 = QtWidgets.QPushButton(self.widget_board)
        self.piece_40.setEnabled(False)
        self.piece_40.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_40.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_40.setText("")
        self.piece_40.setCheckable(False)
        self.piece_40.setProperty("type", "")
        self.piece_40.setProperty("color", "")
        self.piece_40.setObjectName("piece_40")
        self.gridLayout.addWidget(self.piece_40, 4, 0, 1, 1)
        self.piece_00 = QtWidgets.QPushButton(self.widget_board)
        self.piece_00.setMinimumSize(QtCore.QSize(64, 64))
        self.piece_00.setMaximumSize(QtCore.QSize(64, 64))
        self.piece_00.setText("")
        self.piece_00.setProperty("type", "")
        self.piece_00.setObjectName("piece_00")
        self.gridLayout.addWidget(self.piece_00, 0, 0, 1, 1)
        self.textEdit_log = QtWidgets.QTextEdit(AN_Chess)
        self.textEdit_log.setGeometry(QtCore.QRect(370, 10, 361, 371))
        self.textEdit_log.setReadOnly(True)
        self.textEdit_log.setObjectName("textEdit_log")
        self.widget_init = QtWidgets.QWidget(AN_Chess)
        self.widget_init.setGeometry(QtCore.QRect(10, 380, 351, 131))
        self.widget_init.setStyleSheet(".QWidget{background-color: rgb(216, 216, 216);}")
        self.widget_init.setObjectName("widget_init")
        self.label_wecolor = QtWidgets.QLabel(self.widget_init)
        self.label_wecolor.setGeometry(QtCore.QRect(12, 38, 71, 31))
        self.label_wecolor.setObjectName("label_wecolor")
        self.comboBox_weColor = QtWidgets.QComboBox(self.widget_init)
        self.comboBox_weColor.setGeometry(QtCore.QRect(92, 40, 71, 25))
        self.comboBox_weColor.setObjectName("comboBox_weColor")
        self.comboBox_weColor.addItem("")
        self.comboBox_weColor.addItem("")
        self.btn_init = QtWidgets.QPushButton(self.widget_init)
        self.btn_init.setGeometry(QtCore.QRect(60, 80, 101, 31))
        self.btn_init.setObjectName("btn_init")
        self.checkBox_youFirst = QtWidgets.QCheckBox(self.widget_init)
        self.checkBox_youFirst.setGeometry(QtCore.QRect(240, 6, 91, 31))
        self.checkBox_youFirst.setObjectName("checkBox_youFirst")
        self.label_diceType = QtWidgets.QLabel(self.widget_init)
        self.label_diceType.setGeometry(QtCore.QRect(12, 14, 72, 15))
        self.label_diceType.setObjectName("label_diceType")
        self.comboBox_diceType = QtWidgets.QComboBox(self.widget_init)
        self.comboBox_diceType.setGeometry(QtCore.QRect(92, 10, 121, 22))
        self.comboBox_diceType.setObjectName("comboBox_diceType")
        self.comboBox_diceType.addItem("")
        self.comboBox_diceType.addItem("")
        self.label_mode = QtWidgets.QLabel(self.widget_init)
        self.label_mode.setGeometry(QtCore.QRect(180, 38, 51, 31))
        self.label_mode.setObjectName("label_mode")
        self.comboBox_mode = QtWidgets.QComboBox(self.widget_init)
        self.comboBox_mode.setGeometry(QtCore.QRect(230, 40, 101, 25))
        self.comboBox_mode.setObjectName("comboBox_mode")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.widget_running = QtWidgets.QWidget(AN_Chess)
        self.widget_running.setGeometry(QtCore.QRect(10, 520, 351, 151))
        self.widget_running.setStyleSheet(".QWidget{background-color: rgb(216, 216, 216);}")
        self.widget_running.setObjectName("widget_running")
        self.btn_pcDice = QtWidgets.QPushButton(self.widget_running)
        self.btn_pcDice.setGeometry(QtCore.QRect(20, 10, 161, 37))
        self.btn_pcDice.setObjectName("btn_pcDice")
        self.label_diceNum = QtWidgets.QLabel(self.widget_running)
        self.label_diceNum.setGeometry(QtCore.QRect(20, 60, 71, 31))
        self.label_diceNum.setObjectName("label_diceNum")
        self.spinBox_diceNum = QtWidgets.QSpinBox(self.widget_running)
        self.spinBox_diceNum.setGeometry(QtCore.QRect(100, 60, 77, 30))
        self.spinBox_diceNum.setMinimum(1)
        self.spinBox_diceNum.setMaximum(6)
        self.spinBox_diceNum.setObjectName("spinBox_diceNum")
        self.btn_weGo = QtWidgets.QPushButton(self.widget_running)
        self.btn_weGo.setGeometry(QtCore.QRect(20, 100, 161, 37))
        self.btn_weGo.setObjectName("btn_weGo")
        self.btn_back = QtWidgets.QPushButton(self.widget_running)
        self.btn_back.setGeometry(QtCore.QRect(210, 60, 121, 37))
        self.btn_back.setObjectName("btn_back")
        self.widget_save = QtWidgets.QWidget(AN_Chess)
        self.widget_save.setGeometry(QtCore.QRect(370, 400, 362, 111))
        self.widget_save.setStyleSheet(".QWidget{background-color: rgb(216, 216, 216);}")
        self.widget_save.setObjectName("widget_save")
        self.label_first = QtWidgets.QLabel(self.widget_save)
        self.label_first.setGeometry(QtCore.QRect(5, 23, 51, 16))
        self.label_first.setObjectName("label_first")
        self.lineEdit_first = QtWidgets.QLineEdit(self.widget_save)
        self.lineEdit_first.setGeometry(QtCore.QRect(60, 21, 71, 21))
        self.lineEdit_first.setObjectName("lineEdit_first")
        self.label_last = QtWidgets.QLabel(self.widget_save)
        self.label_last.setGeometry(QtCore.QRect(5, 50, 51, 20))
        self.label_last.setObjectName("label_last")
        self.lineEdit_last = QtWidgets.QLineEdit(self.widget_save)
        self.lineEdit_last.setGeometry(QtCore.QRect(60, 50, 71, 21))
        self.lineEdit_last.setObjectName("lineEdit_last")
        self.btn_save = QtWidgets.QPushButton(self.widget_save)
        self.btn_save.setGeometry(QtCore.QRect(170, 80, 90, 25))
        self.btn_save.setObjectName("btn_save")
        self.comboBox_win = QtWidgets.QComboBox(self.widget_save)
        self.comboBox_win.setGeometry(QtCore.QRect(80, 80, 81, 25))
        self.comboBox_win.setObjectName("comboBox_win")
        self.comboBox_win.addItem("")
        self.comboBox_win.addItem("")
        self.lineEdit_place = QtWidgets.QLineEdit(self.widget_save)
        self.lineEdit_place.setGeometry(QtCore.QRect(195, 21, 141, 21))
        self.lineEdit_place.setText("")
        self.lineEdit_place.setObjectName("lineEdit_place")
        self.label_first_2 = QtWidgets.QLabel(self.widget_save)
        self.label_first_2.setGeometry(QtCore.QRect(150, 23, 41, 16))
        self.label_first_2.setObjectName("label_first_2")
        self.label_first_3 = QtWidgets.QLabel(self.widget_save)
        self.label_first_3.setGeometry(QtCore.QRect(150, 50, 41, 16))
        self.label_first_3.setObjectName("label_first_3")
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget_save)
        self.lineEdit_name.setGeometry(QtCore.QRect(195, 50, 141, 21))
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.widget_state = QtWidgets.QWidget(AN_Chess)
        self.widget_state.setGeometry(QtCore.QRect(370, 520, 361, 151))
        self.widget_state.setStyleSheet(".QWidget{background-color: rgb(216, 216, 216);}")
        self.widget_state.setObjectName("widget_state")
        self.label_status = QtWidgets.QLabel(self.widget_state)
        self.label_status.setGeometry(QtCore.QRect(140, 10, 72, 15))
        self.label_status.setObjectName("label_status")
        self.textEdit_status = QtWidgets.QTextEdit(self.widget_state)
        self.textEdit_status.setGeometry(QtCore.QRect(40, 40, 281, 101))
        self.textEdit_status.setReadOnly(True)
        self.textEdit_status.setMarkdown("")
        self.textEdit_status.setObjectName("textEdit_status")
        self.btn_restart = QtWidgets.QPushButton(AN_Chess)
        self.btn_restart.setGeometry(QtCore.QRect(203, 460, 101, 31))
        self.btn_restart.setObjectName("btn_restart")
        self.widget_board_blue_y = QtWidgets.QWidget(AN_Chess)
        self.widget_board_blue_y.setGeometry(QtCore.QRect(-6, 20, 21, 321))
        self.widget_board_blue_y.setObjectName("widget_board_blue_y")
        self.label_y3 = QtWidgets.QLabel(self.widget_board_blue_y)
        self.label_y3.setGeometry(QtCore.QRect(10, 210, 21, 20))
        self.label_y3.setObjectName("label_y3")
        self.label_y2 = QtWidgets.QLabel(self.widget_board_blue_y)
        self.label_y2.setGeometry(QtCore.QRect(10, 150, 21, 20))
        self.label_y2.setObjectName("label_y2")
        self.label_y0 = QtWidgets.QLabel(self.widget_board_blue_y)
        self.label_y0.setGeometry(QtCore.QRect(10, 25, 16, 20))
        self.label_y0.setObjectName("label_y0")
        self.label_y4 = QtWidgets.QLabel(self.widget_board_blue_y)
        self.label_y4.setGeometry(QtCore.QRect(10, 278, 21, 20))
        self.label_y4.setObjectName("label_y4")
        self.label_y1 = QtWidgets.QLabel(self.widget_board_blue_y)
        self.label_y1.setGeometry(QtCore.QRect(10, 80, 21, 20))
        self.label_y1.setObjectName("label_y1")
        self.widget_board_blue_x = QtWidgets.QWidget(AN_Chess)
        self.widget_board_blue_x.setGeometry(QtCore.QRect(20, 340, 321, 31))
        self.widget_board_blue_x.setObjectName("widget_board_blue_x")
        self.label_xB = QtWidgets.QLabel(self.widget_board_blue_x)
        self.label_xB.setGeometry(QtCore.QRect(85, 4, 21, 20))
        self.label_xB.setObjectName("label_xB")
        self.label_xC = QtWidgets.QLabel(self.widget_board_blue_x)
        self.label_xC.setGeometry(QtCore.QRect(153, 4, 21, 20))
        self.label_xC.setObjectName("label_xC")
        self.label_xD = QtWidgets.QLabel(self.widget_board_blue_x)
        self.label_xD.setGeometry(QtCore.QRect(220, 4, 16, 20))
        self.label_xD.setObjectName("label_xD")
        self.label_xE = QtWidgets.QLabel(self.widget_board_blue_x)
        self.label_xE.setGeometry(QtCore.QRect(280, 4, 21, 20))
        self.label_xE.setObjectName("label_xE")
        self.label_xA = QtWidgets.QLabel(self.widget_board_blue_x)
        self.label_xA.setGeometry(QtCore.QRect(23, 4, 21, 20))
        self.label_xA.setObjectName("label_xA")
        self.widget_board_red_x = QtWidgets.QWidget(AN_Chess)
        self.widget_board_red_x.setGeometry(QtCore.QRect(20, -10, 321, 31))
        self.widget_board_red_x.setObjectName("widget_board_red_x")
        self.label_x1_4 = QtWidgets.QLabel(self.widget_board_red_x)
        self.label_x1_4.setGeometry(QtCore.QRect(85, 10, 21, 20))
        self.label_x1_4.setObjectName("label_x1_4")
        self.label_x2_4 = QtWidgets.QLabel(self.widget_board_red_x)
        self.label_x2_4.setGeometry(QtCore.QRect(153, 10, 21, 20))
        self.label_x2_4.setObjectName("label_x2_4")
        self.label_x3_4 = QtWidgets.QLabel(self.widget_board_red_x)
        self.label_x3_4.setGeometry(QtCore.QRect(220, 10, 16, 20))
        self.label_x3_4.setObjectName("label_x3_4")
        self.label_x4_4 = QtWidgets.QLabel(self.widget_board_red_x)
        self.label_x4_4.setGeometry(QtCore.QRect(280, 10, 21, 20))
        self.label_x4_4.setObjectName("label_x4_4")
        self.label_x0_4 = QtWidgets.QLabel(self.widget_board_red_x)
        self.label_x0_4.setGeometry(QtCore.QRect(23, 10, 21, 20))
        self.label_x0_4.setObjectName("label_x0_4")
        self.widget_board_red_y = QtWidgets.QWidget(AN_Chess)
        self.widget_board_red_y.setGeometry(QtCore.QRect(340, 20, 21, 321))
        self.widget_board_red_y.setObjectName("widget_board_red_y")
        self.label_y3_3 = QtWidgets.QLabel(self.widget_board_red_y)
        self.label_y3_3.setGeometry(QtCore.QRect(10, 210, 21, 20))
        self.label_y3_3.setObjectName("label_y3_3")
        self.label_y2_3 = QtWidgets.QLabel(self.widget_board_red_y)
        self.label_y2_3.setGeometry(QtCore.QRect(10, 150, 21, 20))
        self.label_y2_3.setObjectName("label_y2_3")
        self.label_y0_3 = QtWidgets.QLabel(self.widget_board_red_y)
        self.label_y0_3.setGeometry(QtCore.QRect(10, 25, 16, 20))
        self.label_y0_3.setObjectName("label_y0_3")
        self.label_y4_3 = QtWidgets.QLabel(self.widget_board_red_y)
        self.label_y4_3.setGeometry(QtCore.QRect(10, 278, 21, 20))
        self.label_y4_3.setObjectName("label_y4_3")
        self.label_y1_3 = QtWidgets.QLabel(self.widget_board_red_y)
        self.label_y1_3.setGeometry(QtCore.QRect(10, 80, 21, 20))
        self.label_y1_3.setObjectName("label_y1_3")

        self.retranslateUi(AN_Chess)
        self.piece_00.clicked.connect(AN_Chess.piece_clicked)
        self.piece_01.clicked.connect(AN_Chess.piece_clicked)
        self.piece_02.clicked.connect(AN_Chess.piece_clicked)
        self.piece_03.clicked.connect(AN_Chess.piece_clicked)
        self.piece_04.clicked.connect(AN_Chess.piece_clicked)
        self.piece_10.clicked.connect(AN_Chess.piece_clicked)
        self.piece_11.clicked.connect(AN_Chess.piece_clicked)
        self.piece_12.clicked.connect(AN_Chess.piece_clicked)
        self.piece_13.clicked.connect(AN_Chess.piece_clicked)
        self.piece_14.clicked.connect(AN_Chess.piece_clicked)
        self.piece_20.clicked.connect(AN_Chess.piece_clicked)
        self.piece_21.clicked.connect(AN_Chess.piece_clicked)
        self.piece_22.clicked.connect(AN_Chess.piece_clicked)
        self.piece_23.clicked.connect(AN_Chess.piece_clicked)
        self.piece_24.clicked.connect(AN_Chess.piece_clicked)
        self.piece_30.clicked.connect(AN_Chess.piece_clicked)
        self.piece_31.clicked.connect(AN_Chess.piece_clicked)
        self.piece_32.clicked.connect(AN_Chess.piece_clicked)
        self.piece_33.clicked.connect(AN_Chess.piece_clicked)
        self.piece_34.clicked.connect(AN_Chess.piece_clicked)
        self.piece_40.clicked.connect(AN_Chess.piece_clicked)
        self.piece_41.clicked.connect(AN_Chess.piece_clicked)
        self.piece_42.clicked.connect(AN_Chess.piece_clicked)
        self.piece_43.clicked.connect(AN_Chess.piece_clicked)
        self.piece_44.clicked.connect(AN_Chess.piece_clicked)
        self.btn_init.clicked.connect(AN_Chess.init_clicked)
        self.btn_restart.clicked.connect(AN_Chess.restart_clicked)
        self.btn_pcDice.clicked.connect(AN_Chess.dice_clicked)
        self.btn_back.clicked.connect(AN_Chess.back_clicked)
        self.btn_weGo.clicked.connect(AN_Chess.ai_go_clicked)
        self.btn_save.clicked.connect(AN_Chess.save_clicked)
        QtCore.QMetaObject.connectSlotsByName(AN_Chess)

    def retranslateUi(self, AN_Chess):
        _translate = QtCore.QCoreApplication.translate
        AN_Chess.setWindowTitle(_translate("AN_Chess", "百思不得棋解"))
        self.piece_20.setProperty("color", _translate("AN_Chess", "Red"))
        self.piece_20.setProperty("redpos", _translate("AN_Chess", "E3"))
        self.piece_20.setProperty("bluepos", _translate("AN_Chess", "A3"))
        self.piece_24.setProperty("color", _translate("AN_Chess", "Blue"))
        self.piece_24.setProperty("redpos", _translate("AN_Chess", "A3"))
        self.piece_24.setProperty("bluepos", _translate("AN_Chess", "E3"))
        self.piece_03.setProperty("redpos", _translate("AN_Chess", "B1"))
        self.piece_03.setProperty("bluepos", _translate("AN_Chess", "D5"))
        self.piece_02.setProperty("color", _translate("AN_Chess", "Red"))
        self.piece_02.setProperty("redpos", _translate("AN_Chess", "C1"))
        self.piece_02.setProperty("bluepos", _translate("AN_Chess", "C5"))
        self.piece_01.setProperty("color", _translate("AN_Chess", "Red"))
        self.piece_01.setProperty("redpos", _translate("AN_Chess", "D1"))
        self.piece_01.setProperty("bluepos", _translate("AN_Chess", "B5"))
        self.piece_34.setProperty("color", _translate("AN_Chess", "Blue"))
        self.piece_34.setProperty("redpos", _translate("AN_Chess", "A4"))
        self.piece_34.setProperty("bluepos", _translate("AN_Chess", "E2"))
        self.piece_42.setProperty("color", _translate("AN_Chess", "Blue"))
        self.piece_42.setProperty("redpos", _translate("AN_Chess", "C5"))
        self.piece_42.setProperty("bluepos", _translate("AN_Chess", "C1"))
        self.piece_10.setProperty("color", _translate("AN_Chess", "Red"))
        self.piece_10.setProperty("redpos", _translate("AN_Chess", "E2"))
        self.piece_10.setProperty("bluepos", _translate("AN_Chess", "A4"))
        self.piece_13.setProperty("redpos", _translate("AN_Chess", "B2"))
        self.piece_13.setProperty("bluepos", _translate("AN_Chess", "D4"))
        self.piece_21.setProperty("redpos", _translate("AN_Chess", "D3"))
        self.piece_21.setProperty("bluepos", _translate("AN_Chess", "B3"))
        self.piece_32.setProperty("redpos", _translate("AN_Chess", "C4"))
        self.piece_32.setProperty("bluepos", _translate("AN_Chess", "C2"))
        self.piece_31.setProperty("redpos", _translate("AN_Chess", "D4"))
        self.piece_31.setProperty("bluepos", _translate("AN_Chess", "B2"))
        self.piece_44.setProperty("color", _translate("AN_Chess", "Blue"))
        self.piece_44.setProperty("redpos", _translate("AN_Chess", "A5"))
        self.piece_44.setProperty("bluepos", _translate("AN_Chess", "E1"))
        self.piece_41.setProperty("redpos", _translate("AN_Chess", "D5"))
        self.piece_41.setProperty("bluepos", _translate("AN_Chess", "B1"))
        self.piece_33.setProperty("color", _translate("AN_Chess", "Blue"))
        self.piece_33.setProperty("redpos", _translate("AN_Chess", "B4"))
        self.piece_33.setProperty("bluepos", _translate("AN_Chess", "D2"))
        self.piece_30.setProperty("redpos", _translate("AN_Chess", "E4"))
        self.piece_30.setProperty("bluepos", _translate("AN_Chess", "A2"))
        self.piece_04.setProperty("redpos", _translate("AN_Chess", "A1"))
        self.piece_04.setProperty("bluepos", _translate("AN_Chess", "E5"))
        self.piece_22.setProperty("redpos", _translate("AN_Chess", "C3"))
        self.piece_22.setProperty("bluepos", _translate("AN_Chess", "C3"))
        self.piece_23.setProperty("redpos", _translate("AN_Chess", "B3"))
        self.piece_23.setProperty("bluepos", _translate("AN_Chess", "D3"))
        self.piece_43.setProperty("color", _translate("AN_Chess", "Blue"))
        self.piece_43.setProperty("redpos", _translate("AN_Chess", "B5"))
        self.piece_43.setProperty("bluepos", _translate("AN_Chess", "D1"))
        self.piece_14.setProperty("redpos", _translate("AN_Chess", "A2"))
        self.piece_14.setProperty("bluepos", _translate("AN_Chess", "E4"))
        self.piece_12.setProperty("redpos", _translate("AN_Chess", "C2"))
        self.piece_12.setProperty("bluepos", _translate("AN_Chess", "C4"))
        self.piece_11.setProperty("color", _translate("AN_Chess", "Red"))
        self.piece_11.setProperty("redpos", _translate("AN_Chess", "D2"))
        self.piece_11.setProperty("bluepos", _translate("AN_Chess", "B4"))
        self.piece_40.setProperty("redpos", _translate("AN_Chess", "E5"))
        self.piece_40.setProperty("bluepos", _translate("AN_Chess", "A1"))
        self.piece_00.setProperty("color", _translate("AN_Chess", "Red"))
        self.piece_00.setProperty("redpos", _translate("AN_Chess", "E1"))
        self.piece_00.setProperty("bluepos", _translate("AN_Chess", "A5"))
        self.textEdit_log.setHtml(_translate("AN_Chess", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_wecolor.setText(_translate("AN_Chess", "我方棋子："))
        self.comboBox_weColor.setItemText(0, _translate("AN_Chess", "蓝色"))
        self.comboBox_weColor.setItemText(1, _translate("AN_Chess", "红色"))
        self.btn_init.setText(_translate("AN_Chess", "初始化"))
        self.checkBox_youFirst.setText(_translate("AN_Chess", "对方先走"))
        self.label_diceType.setText(_translate("AN_Chess", "骰子方式："))
        self.comboBox_diceType.setItemText(0, _translate("AN_Chess", "电脑掷骰子"))
        self.comboBox_diceType.setItemText(1, _translate("AN_Chess", "人工输入骰子数"))
        self.label_mode.setText(_translate("AN_Chess", "模式："))
        self.comboBox_mode.setItemText(0, _translate("AN_Chess", "Simulation"))
        self.comboBox_mode.setItemText(1, _translate("AN_Chess", "DQN"))
        self.btn_pcDice.setText(_translate("AN_Chess", "电脑掷骰子"))
        self.label_diceNum.setText(_translate("AN_Chess", "骰子点数："))
        self.btn_weGo.setText(_translate("AN_Chess", "我方走子"))
        self.btn_back.setText(_translate("AN_Chess", "悔棋"))
        self.label_first.setText(_translate("AN_Chess", "先手队:"))
        self.label_last.setText(_translate("AN_Chess", "后手队："))
        self.btn_save.setText(_translate("AN_Chess", "保存棋谱"))
        self.comboBox_win.setItemText(0, _translate("AN_Chess", "先手胜"))
        self.comboBox_win.setItemText(1, _translate("AN_Chess", "后手胜"))
        self.label_first_2.setText(_translate("AN_Chess", "地点："))
        self.label_first_3.setText(_translate("AN_Chess", "赛事："))
        self.label_status.setText(_translate("AN_Chess", "当前状态"))
        self.textEdit_status.setHtml(_translate("AN_Chess", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_restart.setText(_translate("AN_Chess", "新的一局"))
        self.label_y3.setText(_translate("AN_Chess", "2"))
        self.label_y2.setText(_translate("AN_Chess", "3"))
        self.label_y0.setText(_translate("AN_Chess", "5"))
        self.label_y4.setText(_translate("AN_Chess", "1"))
        self.label_y1.setText(_translate("AN_Chess", "4"))
        self.label_xB.setText(_translate("AN_Chess", "B"))
        self.label_xC.setText(_translate("AN_Chess", "C"))
        self.label_xD.setText(_translate("AN_Chess", "D"))
        self.label_xE.setText(_translate("AN_Chess", "E"))
        self.label_xA.setText(_translate("AN_Chess", "A"))
        self.label_x1_4.setText(_translate("AN_Chess", "D"))
        self.label_x2_4.setText(_translate("AN_Chess", "C"))
        self.label_x3_4.setText(_translate("AN_Chess", "B"))
        self.label_x4_4.setText(_translate("AN_Chess", "A"))
        self.label_x0_4.setText(_translate("AN_Chess", "E"))
        self.label_y3_3.setText(_translate("AN_Chess", "4"))
        self.label_y2_3.setText(_translate("AN_Chess", "3"))
        self.label_y0_3.setText(_translate("AN_Chess", "1"))
        self.label_y4_3.setText(_translate("AN_Chess", "5"))
        self.label_y1_3.setText(_translate("AN_Chess", "2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AN_Chess = QtWidgets.QWidget()
    ui = Ui_AN_Chess()
    ui.setupUi(AN_Chess)
    AN_Chess.show()
    sys.exit(app.exec_())
