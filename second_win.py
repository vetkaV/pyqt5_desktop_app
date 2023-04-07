from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class TestWin(QWidget):
    def __init__ (self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        
