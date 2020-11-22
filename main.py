from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
import random
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        uic.loadUi('UI.ui', self)
        self.DrawButton.clicked.connect(self.draw)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawcircle(qp)
            qp.end()
            self.flag = False
            
    def draw(self):
        self.flag = True
        self.repaint()

    def drawcircle(self, qp):
        qp.setBrush(QColor('yellow'))
        r = random.randint(15, 150)
        x = random.randint(15, 380 - r // 2)
        y = random.randint(15, 300 - r // 2)
        qp.drawEllipse(x, y, r, r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())    
        
