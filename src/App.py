import sys
from PyQt5.QtWidgets import *
from EGEaudioRec.src.FirstForm import FirstForm


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        f = FirstForm()
        hbox = QHBoxLayout(self)
        hbox.addWidget(f)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    #w = firstForm()
    #w.resize(1300, 700)
    #qtRectangle = w.frameGeometry()
    #centerPoint = QDesktopWidget().availableGeometry().center()
    #qtRectangle.moveCenter(centerPoint)
    #w.move(qtRectangle.topLeft())
    #w.setWindowTitle('E-Learning')
    #w.showMaximized()
    form.showMaximized()
    app.exec_()




