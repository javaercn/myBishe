from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import *

class myLabel(QLabel):
    def __init__(self,o):
        super(myLabel,self).__init__(o)
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()