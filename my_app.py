from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApllication,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

