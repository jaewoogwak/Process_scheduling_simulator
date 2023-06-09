import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from qt_material import apply_stylesheet
#from qt_material import apply_stylesheet, QtStyleTools
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
import FCFS
import HRRN
import RPN
import RR
import SPN

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.processnum = -1
        self.pushButton_core1.clicked.connect(self.click_core1)
        self.pushButton_core2.clicked.connect(self.click_core2)
        self.pushButton_core3.clicked.connect(self.click_core3)
        self.pushButton_core4.clicked.connect(self.click_core4)
        self.pushButton_padd.clicked.connect(self.click_padd)
        self.pushButton_podd.clicked.connect(self.click_podd)
    
    def setupUi(self, Dialog): #ui 모음
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(490, 60, 120, 40))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(10, 100, 240, 40))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(227, 233, 239);\n"
"alternate-background-color: rgb(227, 233, 239);\n"
"border-color: rgb(227, 233, 239);\n"
"color: rgb(18, 67, 112);")
        self.comboBox.setEditable(False)
        self.comboBox.setIconSize(QtCore.QSize(20, 20))
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 480, 60))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 120, 40))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.time_quantum = QtWidgets.QPlainTextEdit(Dialog)
        self.time_quantum.setGeometry(QtCore.QRect(260, 100, 120, 40))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.time_quantum.setFont(font)
        self.time_quantum.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time_quantum.setStyleSheet("background-color: rgb(227, 233, 239);\n"
"border-color: rgb(255, 255, 255);")
        self.time_quantum.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.time_quantum.setFrameShadow(QtWidgets.QFrame.Plain)
        self.time_quantum.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.time_quantum.setReadOnly(False)
        self.time_quantum.setPlainText("")
        self.time_quantum.setObjectName("time_quantum")
        self.pushButton_Run = QtWidgets.QPushButton(Dialog)
        self.pushButton_Run.setGeometry(QtCore.QRect(390, 100, 80, 40))
        self.pushButton_Run.setStyleSheet("\n"
"background-color: rgb(227, 233, 239);")
        self.pushButton_Run.setObjectName("pushButton_Run")
        self.label_readyqueue = QtWidgets.QLabel(Dialog)
        self.label_readyqueue.setGeometry(QtCore.QRect(490, 100, 780, 40))
        self.label_readyqueue.setStyleSheet("background-color: rgb(227, 233, 239);")
        self.label_readyqueue.setText("")
        self.label_readyqueue.setObjectName("label_readyqueue")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 120, 40))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(490, 180, 120, 40))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(490, 460, 120, 40))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 460, 120, 40))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(1000, 460, 50, 40))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(1100, 460, 90, 40))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(1120, 10, 160, 40))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushButton_core1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_core1.setGeometry(QtCore.QRect(20, 230, 75, 75))
        self.pushButton_core1.setStyleSheet("background-color: rgb(227, 233, 239);")
        self.pushButton_core1.setObjectName("pushButton_core1")
        self.pushButton_core2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_core2.setGeometry(QtCore.QRect(260, 230, 75, 75))
        self.pushButton_core2.setStyleSheet("background-color: rgb(227, 233, 239);")
        self.pushButton_core2.setObjectName("pushButton_core2")
        self.pushButton_core3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_core3.setGeometry(QtCore.QRect(20, 350, 75, 75))
        self.pushButton_core3.setStyleSheet("background-color: rgb(227, 233, 239);")
        self.pushButton_core3.setObjectName("pushButton_core3")
        self.pushButton_core4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_core4.setGeometry(QtCore.QRect(260, 350, 75, 75))
        self.pushButton_core4.setStyleSheet("background-color: rgb(227, 233, 239);")
        self.pushButton_core4.setObjectName("pushButton_core4")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(140, 235, 80, 20))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_usagewatt = QtWidgets.QLabel(Dialog)
        self.label_usagewatt.setGeometry(QtCore.QRect(1190, 460, 80, 40))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(10)
        self.label_usagewatt.setFont(font)
        self.label_usagewatt.setObjectName("label_usagewatt")
        self.label_nowtime = QtWidgets.QLabel(Dialog)
        self.label_nowtime.setGeometry(QtCore.QRect(1050, 460, 50, 40))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(10)
        self.label_nowtime.setFont(font)
        self.label_nowtime.setObjectName("label_nowtime")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(140, 350, 80, 20))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(380, 350, 80, 20))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(380, 235, 80, 20))
        font = QtGui.QFont()
        font.setFamily("HY헤드라인M")
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.pushButton_core1p = QtWidgets.QPushButton(Dialog)
        self.pushButton_core1p.setGeometry(QtCore.QRect(140, 260, 80, 20))
        self.pushButton_core1p.setStyleSheet("background-color: rgb(227, 233, 239);")
        self.pushButton_core1p.setObjectName("pushButton_core1p")
        self.pushButton_core2p = QtWidgets.QPushButton(Dialog)
        self.pushButton_core2p.setGeometry(QtCore.QRect(380, 260, 80, 20))
        self.pushButton_core2p.setStyleSheet("background-color: rgb(227, 233, 239);")
        self.pushButton_core2p.setObjectName("pushButton_core2p")
        self.pushButton_core4p = QtWidgets.QPushButton(Dialog)
        self.pushButton_core4p.setGeometry(QtCore.QRect(380, 375, 80, 20))
        self.pushButton_core4p.setStyleSheet("background-color: rgb(227, 233, 239);")
        self.pushButton_core4p.setObjectName("pushButton_core4p")
        self.pushButton_core3p = QtWidgets.QPushButton(Dialog)
        self.pushButton_core3p.setGeometry(QtCore.QRect(140, 375, 80, 20))
        self.pushButton_core3p.setStyleSheet("\n"
"background-color: rgb(227, 233, 239);\n"
"")
        self.pushButton_core3p.setObjectName("pushButton_core3p")
        self.pushButton_core1e = QtWidgets.QPushButton(Dialog)
        self.pushButton_core1e.setGeometry(QtCore.QRect(140, 285, 80, 20))
        self.pushButton_core1e.setStyleSheet("background-color: rgb(227, 233, 239);")
        self.pushButton_core1e.setObjectName("pushButton_core1e")
        self.pushButton_core2e = QtWidgets.QPushButton(Dialog)
        self.pushButton_core2e.setGeometry(QtCore.QRect(380, 285, 80, 20))
        self.pushButton_core2e.setStyleSheet("background-color: rgb(227, 233, 239);")
        self.pushButton_core2e.setObjectName("pushButton_core2e")
        self.pushButton_core3e = QtWidgets.QPushButton(Dialog)
        self.pushButton_core3e.setGeometry(QtCore.QRect(140, 400, 80, 20))
        self.pushButton_core3e.setStyleSheet("background-color: rgb(227, 233, 239);")
        self.pushButton_core3e.setObjectName("pushButton_core3e")
        self.pushButton_core4e = QtWidgets.QPushButton(Dialog)
        self.pushButton_core4e.setGeometry(QtCore.QRect(380, 400, 80, 20))
        self.pushButton_core4e.setStyleSheet("background-color: rgb(227, 233, 239);")
        self.pushButton_core4e.setObjectName("pushButton_core4e")
        self.tableWidget_process = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_process.setGeometry(QtCore.QRect(10, 500, 460, 200))
        self.tableWidget_process.setStyleSheet("")
        self.tableWidget_process.setObjectName("tableWidget_process")
        self.tableWidget_process.setColumnCount(2)
        self.tableWidget_process.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(227, 233, 239, 0))
        self.tableWidget_process.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(227, 233, 239))
        self.tableWidget_process.setHorizontalHeaderItem(1, item)
        #테이블 칸 꽉채우기
        header = self.tableWidget_process.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_gantt = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_gantt.setGeometry(QtCore.QRect(490, 230, 780, 220))
        self.tableWidget_gantt.setObjectName("tableWidget_gantt")
        self.tableWidget_gantt.setColumnCount(0)
        self.tableWidget_gantt.setRowCount(0)
        self.tableWidget_result = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_result.setGeometry(QtCore.QRect(490, 500, 780, 200))
        self.tableWidget_result.setObjectName("tableWidget_result")
        self.tableWidget_result.setColumnCount(6)
        self.tableWidget_result.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(5, item)
        self.pushButton_padd = QtWidgets.QPushButton(Dialog)
        self.pushButton_padd.setGeometry(QtCore.QRect(140, 460, 40, 40))
        self.pushButton_padd.setStyleSheet("background-color: rgb(227, 233, 239);")
        self.pushButton_padd.setObjectName("pushButton_padd")
        self.pushButton_podd = QtWidgets.QPushButton(Dialog)
        self.pushButton_podd.setGeometry(QtCore.QRect(190, 460, 40, 40))
        self.pushButton_podd.setStyleSheet("background-color: rgb(227, 233, 239);")
        self.pushButton_podd.setObjectName("pushButton_podd")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog): #초기값 설정
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Ready Queue"))
        self.comboBox.setCurrentText(_translate("Dialog", "FCFS"))
        self.comboBox.setItemText(0, _translate("Dialog", "FCFS"))
        self.comboBox.setItemText(1, _translate("Dialog", "Round Robin"))
        self.comboBox.setItemText(2, _translate("Dialog", "SPN"))
        self.comboBox.setItemText(3, _translate("Dialog", "SRTN"))
        self.comboBox.setItemText(4, _translate("Dialog", "HRRN"))
        self.comboBox.setItemText(5, _translate("Dialog", "RPN"))
        self.label.setText(_translate("Dialog", "Process Scheduling Simulator"))
        self.label_2.setText(_translate("Dialog", "Algorithm"))
        self.pushButton_Run.setText(_translate("Dialog", "RUN"))
        self.label_5.setText(_translate("Dialog", "Processor"))
        self.label_6.setText(_translate("Dialog", "Gantt Chart"))
        self.label_7.setText(_translate("Dialog", "Result"))
        self.label_8.setText(_translate("Dialog", "Process"))
        self.label_9.setText(_translate("Dialog", "시간 :"))
        self.label_10.setText(_translate("Dialog", "소비 전력 :"))
        self.label_11.setText(_translate("Dialog", "Team : OhYes"))
        self.pushButton_core1.setText(_translate("Dialog", "OFF"))
        self.pushButton_core2.setText(_translate("Dialog", "OFF"))
        self.pushButton_core3.setText(_translate("Dialog", "OFF"))
        self.pushButton_core4.setText(_translate("Dialog", "OFF"))
        self.label_12.setText(_translate("Dialog", "CORE 1"))
        self.label_usagewatt.setText(_translate("Dialog", "watt"))
        self.label_nowtime.setText(_translate("Dialog", "time"))
        self.label_19.setText(_translate("Dialog", "CORE 3"))
        self.label_20.setText(_translate("Dialog", "CORE 4"))
        self.label_23.setText(_translate("Dialog", "CORE 2"))
        self.pushButton_core1p.setText(_translate("Dialog", "P-CORE"))
        self.pushButton_core2p.setText(_translate("Dialog", "P-CORE"))
        self.pushButton_core4p.setText(_translate("Dialog", "P-CORE"))
        self.pushButton_core3p.setText(_translate("Dialog", "P-CORE"))
        self.pushButton_core1e.setText(_translate("Dialog", "E-CORE"))
        self.pushButton_core2e.setText(_translate("Dialog", "E-CORE"))
        self.pushButton_core3e.setText(_translate("Dialog", "E-CORE"))
        self.pushButton_core4e.setText(_translate("Dialog", "E-CORE"))
        item = self.tableWidget_process.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ARRIVAL TIME"))
        item = self.tableWidget_process.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "LOAD TIME"))
        item = self.tableWidget_result.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "AT"))
        item = self.tableWidget_result.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "BT"))
        item = self.tableWidget_result.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "WT"))
        item = self.tableWidget_result.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "TT"))
        item = self.tableWidget_result.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "NTT"))
        item = self.tableWidget_result.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "DONE"))
        self.pushButton_padd.setText(_translate("Dialog", "+"))
        self.pushButton_podd.setText(_translate("Dialog", "-"))

    def moveui(self): #창을 옮기는 함수
        self.move_to_center()
    def move_to_center(self): #창을 가운데로 옮김
        screen = QDesktopWidget().screenGeometry()
        window = self.geometry()
        self.move((screen.width()-window.width())/2, (screen.height()-window.height())/2)

    def click_core1(self):
        global core1
        if core1 % 2 == 0:
            self.pushButton_core1.setText("ON")
            self.pushButton_core1.setStyleSheet("color: rgb(255,255,255); background-color: rgb(18, 67, 112);")
        else:
            self.pushButton_core1.setText("OFF")
            self.pushButton_core1.setStyleSheet("background-color: rgb(227, 233, 239);")
        core1 += 1

    def click_core2(self):
        global core2
        if core2 % 2 == 0:
            self.pushButton_core2.setText("ON")
            self.pushButton_core2.setStyleSheet("color: rgb(255,255,255);background-color: rgb(18, 67, 112);")
        else:
            self.pushButton_core2.setText("OFF")
            self.pushButton_core2.setStyleSheet("background-color: rgb(227, 233, 239);")
        core2 += 1

    def click_core3(self):
        global core3
        if core3 % 2 == 0:
            self.pushButton_core3.setText("ON")
            self.pushButton_core3.setStyleSheet("color: rgb(255,255,255);background-color: rgb(18, 67, 112);")
        else:
            self.pushButton_core3.setText("OFF")
            self.pushButton_core3.setStyleSheet("background-color: rgb(227, 233, 239);")
        core3 += 1

    def click_core4(self):
        global core4
        if core4 % 2 == 0:
            self.pushButton_core4.setText("ON")
            self.pushButton_core4.setStyleSheet("color: rgb(255,255,255);background-color: rgb(18, 67, 112);")
        else:
            self.pushButton_core4.setText("OFF")
            self.pushButton_core4.setStyleSheet("background-color: rgb(227, 233, 239);")
        core4 += 1

    def click_padd(self):
        _translate = QtCore.QCoreApplication.translate
        if self.processnum < 14:
            self.processnum += 1
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_process.setVerticalHeaderItem(self.processnum, item)
        self.tableWidget_result.setVerticalHeaderItem(self.processnum, item)
        item = self.tableWidget_process.verticalHeaderItem(self.processnum)
        item = self.tableWidget_result.verticalHeaderItem(self.processnum)
        item.setText(_translate("Dialog", "P{}".format(self.processnum+1)))
    
    def click_podd(self):
        if self.processnum != -1:
            item = QtWidgets.QTableWidgetItem('')
            self.tableWidget_process.setVerticalHeaderItem(self.processnum, item)
            self.tableWidget_result.setVerticalHeaderItem(self.processnum, item)
            if self.processnum >= 0:
                self.processnum -= 1
            
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
    global core1,core2,core3,core4,c1p,c1e,c2p,c2e,c3p,c3e,c4p,c4e
    core1,core2,core3,core4,c1p,c1e,c2p,c2e,c3p,c3e,c4p,c4e = 0,0,0,0,0,0,0,0,0,0,0,0

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()