from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
import random
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.flag = False
        uic.loadUi('UI.ui', self)
        self.DrawButton.clicked.connect(self.draw)

    def paintEvent(self):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(0, 255, 255))
            r = random.randint(15, 150)
            x = random.randint(15, 380 - r / 2)
            y = random.randint(15, 300 - r / 2)
            qp.drawEllipse(100, 100, 50, 50)
            qp.end()
            
    def draw(self):
        pass
        #sel.flag = True
        #self.repaint()
        #print(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())    
        
