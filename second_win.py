from instr import *
from PyQt5.QtCore import Qt,QTimer,QTime 
from PyQt5.QtWidgets import *
from results import *
from PyQt5.QtGui import QFont


class TestWin(QWidget):
    def __init__ (self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize (win_width, win_height)
        self.move(win_x, win_y)
    
    def initUI(self):
        self.you_name = QLabel(txt_name)
        self.blank1 = QLineEdit(txt_hintname)
        self.age = QLabel (txt_age)
        self.blank2 = QLineEdit (txt_hinttest1)
        self.instruction_test1 = QLabel(txt_test1)
        self.first_button = QPushButton (txt_starttest1)
        self.blank3 = QLineEdit (txt_hinttest2)
        self.instruction_test2 = QLabel (txt_test2)
        self.second_button = QPushButton (txt_starttest2)
        self.instruction_test3 = QLabel (txt_test3)
        self.thirts_button = QPushButton (txt_starttest3)
        self.blank4 = QLineEdit (txt_hinttest3)
        self.blank5 = QLineEdit (txt_hinttest3)
        self.fours_button = QPushButton (txt_sendresults)
        self.text_timer = QLabel (txt_timer)
        self.h_line = QHBoxLayout()
        self.v_line1 = QVBoxLayout()
        self.v_line2 = QVBoxLayout()
        self.v_line1.addWidget(self.you_name)
        self.v_line1.addWidget(self.blank1)
        self.v_line1.addWidget(self.age)
        self.v_line1.addWidget(self.blank2)
        self.v_line1.addWidget(self.instruction_test1)
        self.v_line1.addWidget(self.first_button)
        self.v_line1.addWidget(self.blank3)
        self.v_line1.addWidget(self.instruction_test2)
        self.v_line1.addWidget(self.second_button)
        self.v_line1.addWidget(self.instruction_test3)
        self.v_line1.addWidget(self.thirts_button)
        self.v_line1.addWidget(self.blank4)
        self.v_line1.addWidget(self.blank5)
        self.v_line1.addWidget(self.fours_button)
        self.v_line2.addWidget(self.text_timer)
        self.h_line.addLayout(self.v_line1, 80)
        self.h_line.addLayout(self.v_line2, 20)
        self.setLayout(self.h_line)
    
    def connects(self):
        self.fours_button.clicked.connect(self.next_click)
        self.first_button.clicked.connect(self.timer_test)
        self.second_button.clicked.connect(self.timer_sits)
        self.thirts_button.clicked.connect(self.timer_final)
    
    def timer1Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times',36,QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss')== '00:00:00':
            self.timer.stop()

    
    def next_click(self):
        self.hide()
        self.next_screen = MainWin()
    
    def timer_test(self):
        global time
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    
    def timer_sits(self):
        global time
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)


    def timer2Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setFont(QFont('Times',36,QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss')[6:8]== '00':
            self.timer.stop()
    
    def timer_final(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times',36,QFont.Bold))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <=15:
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        else:
            self.text_timer.setStyleSheet('color: rgb(0,0,0)')
        
    
