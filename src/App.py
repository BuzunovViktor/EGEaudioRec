import sys

from PyQt5.QtWidgets import *
from EGEaudioRec.src.FirstForm import FirstForm


class MainForm(QWidget):
    def __init__(self):
        super().__init__()

        f = FirstForm()
        hbox = QHBoxLayout(self)
        #self.setStyleSheet("background-color:#FFF;")
        #self.setStyleSheet("background-image: url('../images/background.jpg'); background-attachment: fixed")
        hbox.addWidget(f)
        #self.setStyleSheet("background-image: url('../images/background.jpg'); background-attachment: cover;")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    #mainWindow = QMainWindow(form)
    #mainWindow.setStyleSheet("background-image: url('../images/background.jpg'); background-attachment: cover;")

    #w = firstForm()
    #w.resize(1300, 700)
    #qtRectangle = w.frameGeometry()
    #centerPoint = QDesktopWidget().availableGeometry().center()
    #qtRectangle.moveCenter(centerPoint)
    #w.move(qtRectangle.topLeft())
    #w.setWindowTitle('E-Learning')
    form.showMaximized()
    #mainWindow.showMaximized()
    app.exec_()




