from PyQt5 import QtCore, QtGui, QtWidgets
from TreeChildren import *

scanned = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 675)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 480, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(60, 520, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(90, 450, 20, 101))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(130, 450, 20, 101))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(60, 450, 118, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(60, 550, 118, 3))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(170, 450, 20, 101))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(50, 450, 20, 101))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(250, 550, 118, 3))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(250, 480, 118, 3))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(360, 450, 20, 101))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(280, 450, 20, 101))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(320, 450, 20, 101))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(250, 520, 118, 3))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(240, 450, 20, 101))
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(250, 450, 118, 3))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_33 = QtWidgets.QFrame(self.centralwidget)
        self.line_33.setGeometry(QtCore.QRect(340, 270, 118, 3))
        self.line_33.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setObjectName("line_33")
        self.line_34 = QtWidgets.QFrame(self.centralwidget)
        self.line_34.setGeometry(QtCore.QRect(340, 190, 118, 3))
        self.line_34.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_34.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_34.setObjectName("line_34")
        self.line_35 = QtWidgets.QFrame(self.centralwidget)
        self.line_35.setGeometry(QtCore.QRect(450, 150, 20, 121))
        self.line_35.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_35.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_35.setObjectName("line_35")
        self.line_36 = QtWidgets.QFrame(self.centralwidget)
        self.line_36.setGeometry(QtCore.QRect(370, 150, 20, 121))
        self.line_36.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_36.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_36.setObjectName("line_36")
        self.line_37 = QtWidgets.QFrame(self.centralwidget)
        self.line_37.setGeometry(QtCore.QRect(410, 150, 20, 121))
        self.line_37.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_37.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_37.setObjectName("line_37")
        self.line_38 = QtWidgets.QFrame(self.centralwidget)
        self.line_38.setGeometry(QtCore.QRect(340, 230, 118, 3))
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.line_39 = QtWidgets.QFrame(self.centralwidget)
        self.line_39.setGeometry(QtCore.QRect(330, 150, 20, 121))
        self.line_39.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_39.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_39.setObjectName("line_39")
        self.line_40 = QtWidgets.QFrame(self.centralwidget)
        self.line_40.setGeometry(QtCore.QRect(340, 150, 118, 3))
        self.line_40.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_40.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_40.setObjectName("line_40")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 120, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(70, 460, 21, 16))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 460, 21, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 460, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 490, 21, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 490, 21, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 490, 21, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 530, 21, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(110, 530, 21, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(150, 530, 21, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(260, 460, 21, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(300, 460, 21, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(340, 460, 21, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(260, 490, 21, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(300, 490, 21, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(340, 490, 21, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(260, 530, 21, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(300, 530, 21, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(340, 530, 21, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(440, 460, 21, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(480, 460, 21, 16))
        self.label_20.setObjectName("label_20")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(430, 550, 118, 3))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(440, 490, 21, 16))
        self.label_22.setObjectName("label_22")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(440, 530, 21, 16))
        self.label_25.setObjectName("label_25")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(430, 480, 118, 3))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.centralwidget)
        self.line_19.setGeometry(QtCore.QRect(540, 450, 20, 101))
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setGeometry(QtCore.QRect(460, 450, 20, 101))
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(self.centralwidget)
        self.line_21.setGeometry(QtCore.QRect(500, 450, 20, 101))
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(480, 530, 21, 16))
        self.label_26.setObjectName("label_26")
        self.line_22 = QtWidgets.QFrame(self.centralwidget)
        self.line_22.setGeometry(QtCore.QRect(430, 520, 118, 3))
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(520, 460, 21, 16))
        self.label_21.setObjectName("label_21")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(520, 530, 21, 16))
        self.label_27.setObjectName("label_27")
        self.line_23 = QtWidgets.QFrame(self.centralwidget)
        self.line_23.setGeometry(QtCore.QRect(420, 450, 20, 101))
        self.line_23.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.line_24 = QtWidgets.QFrame(self.centralwidget)
        self.line_24.setGeometry(QtCore.QRect(430, 450, 118, 3))
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(480, 490, 21, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(520, 490, 21, 16))
        self.label_24.setObjectName("label_24")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(630, 460, 21, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(670, 460, 21, 16))
        self.label_29.setObjectName("label_29")
        self.line_25 = QtWidgets.QFrame(self.centralwidget)
        self.line_25.setGeometry(QtCore.QRect(620, 550, 118, 3))
        self.line_25.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(630, 490, 21, 16))
        self.label_31.setObjectName("label_31")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(630, 530, 21, 16))
        self.label_34.setObjectName("label_34")
        self.line_26 = QtWidgets.QFrame(self.centralwidget)
        self.line_26.setGeometry(QtCore.QRect(620, 480, 118, 3))
        self.line_26.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.line_27 = QtWidgets.QFrame(self.centralwidget)
        self.line_27.setGeometry(QtCore.QRect(730, 450, 20, 101))
        self.line_27.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.line_28 = QtWidgets.QFrame(self.centralwidget)
        self.line_28.setGeometry(QtCore.QRect(650, 450, 20, 101))
        self.line_28.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.line_41 = QtWidgets.QFrame(self.centralwidget)
        self.line_41.setGeometry(QtCore.QRect(690, 450, 20, 101))
        self.line_41.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(670, 530, 21, 16))
        self.label_35.setObjectName("label_35")
        self.line_30 = QtWidgets.QFrame(self.centralwidget)
        self.line_30.setGeometry(QtCore.QRect(620, 520, 118, 3))
        self.line_30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(710, 460, 21, 16))
        self.label_30.setObjectName("label_30")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(710, 530, 21, 16))
        self.label_36.setObjectName("label_36")
        self.line_31 = QtWidgets.QFrame(self.centralwidget)
        self.line_31.setGeometry(QtCore.QRect(610, 450, 20, 101))
        self.line_31.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.line_32 = QtWidgets.QFrame(self.centralwidget)
        self.line_32.setGeometry(QtCore.QRect(620, 450, 118, 3))
        self.line_32.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_32.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_32.setObjectName("line_32")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(670, 490, 21, 16))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(710, 490, 21, 16))
        self.label_33.setObjectName("label_33")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 310, 201, 71))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(350, 160, 21, 22))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 160, 21, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(430, 160, 21, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(350, 200, 21, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(390, 200, 21, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(430, 200, 21, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(350, 240, 21, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(390, 240, 21, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(430, 240, 21, 22))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton.clicked.connect(lambda: print(Tree.TreeScan(tree,
                                                              self.lineEdit_1.text(),
                                                              self.lineEdit_2.text(),
                                                              self.lineEdit_3.text(),
                                                              self.lineEdit_4.text(),
                                                              self.lineEdit_5.text(),
                                                              self.lineEdit_6.text(),
                                                              self.lineEdit_7.text(),
                                                              self.lineEdit_8.text(),
                                                              self.lineEdit_9.text())))
        self.pushButton.clicked.connect(self.PrintTrees)
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(60, 570, 55, 16))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(60, 600, 55, 16))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(250, 570, 55, 16))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(250, 600, 55, 16))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(440, 570, 55, 16))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setGeometry(QtCore.QRect(440, 600, 55, 16))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.centralwidget)
        self.label_43.setGeometry(QtCore.QRect(620, 570, 55, 16))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        self.label_44.setGeometry(QtCore.QRect(620, 600, 55, 16))
        self.label_44.setObjectName("label_44")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tree:"))
        self.label_1.setText(_translate("MainWindow", " "))
        self.label_2.setText(_translate("MainWindow", " "))
        self.label_3.setText(_translate("MainWindow", " "))
        self.label_4.setText(_translate("MainWindow", " "))
        self.label_5.setText(_translate("MainWindow", " "))
        self.label_6.setText(_translate("MainWindow", " "))
        self.label_7.setText(_translate("MainWindow", " "))
        self.label_8.setText(_translate("MainWindow", " "))
        self.label_9.setText(_translate("MainWindow", " "))
        self.label_10.setText(_translate("MainWindow", " "))
        self.label_11.setText(_translate("MainWindow", " "))
        self.label_12.setText(_translate("MainWindow", " "))
        self.label_13.setText(_translate("MainWindow", " "))
        self.label_14.setText(_translate("MainWindow", " "))
        self.label_15.setText(_translate("MainWindow", " "))
        self.label_16.setText(_translate("MainWindow", " "))
        self.label_17.setText(_translate("MainWindow", " "))
        self.label_18.setText(_translate("MainWindow", " "))
        self.label_19.setText(_translate("MainWindow", " "))
        self.label_20.setText(_translate("MainWindow", " "))
        self.label_21.setText(_translate("MainWindow", " "))
        self.label_22.setText(_translate("MainWindow", " "))
        self.label_23.setText(_translate("MainWindow", " "))
        self.label_24.setText(_translate("MainWindow", " "))
        self.label_25.setText(_translate("MainWindow", " "))
        self.label_26.setText(_translate("MainWindow", " "))
        self.label_27.setText(_translate("MainWindow", " "))
        self.label_28.setText(_translate("MainWindow", " "))
        self.label_29.setText(_translate("MainWindow", " "))
        self.label_30.setText(_translate("MainWindow", " "))
        self.label_31.setText(_translate("MainWindow", " "))
        self.label_32.setText(_translate("MainWindow", " "))
        self.label_33.setText(_translate("MainWindow", " "))
        self.label_34.setText(_translate("MainWindow", " "))
        self.label_35.setText(_translate("MainWindow", " "))
        self.label_36.setText(_translate("MainWindow", " "))
        self.label_37.setText(_translate("MainWindow", " "))
        self.label_38.setText(_translate("MainWindow", " "))
        self.label_39.setText(_translate("MainWindow", " "))
        self.label_40.setText(_translate("MainWindow", " "))
        self.label_41.setText(_translate("MainWindow", " "))
        self.label_42.setText(_translate("MainWindow", " "))
        self.label_43.setText(_translate("MainWindow", " "))
        self.label_44.setText(_translate("MainWindow", " "))
        self.pushButton.setText(_translate("MainWindow", "Get Children"))

    def PrintTrees(self):

        #CLEAR ALL TREES
        x, y = 1, 1
        for i in range(1,45):
            label = eval('self.label_' + str(i))
            label.setText(" ")
                    
        if len(trees)==2:
            x, y = 1, 1
            for i in range(1,10):
                label = eval('self.label_' + str(i))
                label.setText(trees[0][str(x)+','+str(y)])
                y+=1
                if y==4:
                    y=1
                    x+=1

            mis1, man1 = Tree.ComputeCostStatic(trees[0])
            self.label_37.setText("Mis: " + str(mis1))
            self.label_38.setText("Man: " + str(man1))

            x, y = 1, 1
            for i in range(10,19):
                label = eval('self.label_' + str(i))
                label.setText(trees[1][str(x)+','+str(y)])
                y+=1
                if y==4:
                    y=1
                    x+=1

            mis2, man2 = Tree.ComputeCostStatic(trees[1])
            self.label_39.setText("Mis: " + str(mis2))
            self.label_40.setText("Man: " + str(man2))
                    
        elif len(trees)==3:
            x, y = 1, 1
            for i in range(1,10):
                label = eval('self.label_' + str(i))
                label.setText(trees[0][str(x)+','+str(y)])
                y+=1
                if y==4:
                    y=1
                    x+=1

            mis1, man1 = Tree.ComputeCostStatic(trees[0])
            self.label_37.setText("Mis: " + str(mis1))
            self.label_38.setText("Man: " + str(man1))

            x, y = 1, 1
            for i in range(10,19):
                label = eval('self.label_' + str(i))
                label.setText(trees[1][str(x)+','+str(y)])
                y+=1
                if y==4:
                    y=1
                    x+=1

            mis2, man2 = Tree.ComputeCostStatic(trees[1])
            self.label_39.setText("Mis: " + str(mis2))
            self.label_40.setText("Man: " + str(man2))

            x, y = 1, 1
            for i in range(19,28):
                label = eval('self.label_' + str(i))
                label.setText(trees[2][str(x)+','+str(y)])
                y+=1
                if y==4:
                    y=1
                    x+=1

            mis3, man3 = Tree.ComputeCostStatic(trees[2])
            self.label_41.setText("Mis: " + str(mis3))
            self.label_42.setText("Man: " + str(man3))

        elif len(trees)==4:
            x, y = 1, 1
            for i in range(1,10):
                label = eval('self.label_' + str(i))
                label.setText(trees[0][str(x)+','+str(y)])
                y+=1
                if y==4:
                    y=1
                    x+=1

            mis1, man1 = Tree.ComputeCostStatic(trees[0])
            self.label_37.setText("Mis: " + str(mis1))
            self.label_38.setText("Man: " + str(man1))

            x, y = 1, 1
            for i in range(10,19):
                label = eval('self.label_' + str(i))
                label.setText(trees[1][str(x)+','+str(y)])
                y+=1
                if y==4:
                    y=1
                    x+=1

            mis2, man2 = Tree.ComputeCostStatic(trees[1])
            self.label_39.setText("Mis: " + str(mis2))
            self.label_40.setText("Man: " + str(man2))


            x, y = 1, 1
            for i in range(19,28):
                label = eval('self.label_' + str(i))
                label.setText(trees[2][str(x)+','+str(y)])
                y+=1
                if y==4:
                    y=1
                    x+=1

            mis3, man3 = Tree.ComputeCostStatic(trees[2])
            self.label_41.setText("Mis: " + str(mis3))
            self.label_42.setText("Man: " + str(man3))
                    
            x,y = 1,1
            for i in range(28,37):
                label = eval('self.label_' + str(i))
                label.setText(trees[3][str(x)+','+str(y)])
                y+=1
                if y==4:
                    y=1
                    x+=1

            mis4, man4 = Tree.ComputeCostStatic(trees[3])
            self.label_43.setText("Mis: " + str(mis4))
            self.label_44.setText("Man: " + str(man4))
                    
        trees.clear()


if __name__ == "__main__":
    import sys
    Tree = TreeChildren()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

