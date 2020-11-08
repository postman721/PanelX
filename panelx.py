#PanelX v.0.1 Copyright (c) 2020 JJ Posti <techtimejourney.net> This program comes with ABSOLUTELY NO WARRANTY; for details see: http://www.gnu.org/copyleft/gpl.html.  This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991")
#!/usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication,QWidget, QLabel, QHBoxLayout
import os,sys
from threading import Timer
import gi
gi.require_version("Wnck", "3.0")
from gi.repository import Wnck

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()
        self.initUI()
    def initUI(self):
        self.setStyleSheet("color:#ffffff; background: transparent;font-size: 12px;")
        self.frameless = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(self.frameless)
        self.tool=QLabel()
        hbox=QHBoxLayout()
        hbox.addWidget(self.tool)
        self.setLayout(hbox)
        self.setGeometry(0, 0, 0, 15)
        self.panel()
        self.show()
        
    def panel(self):
        scr = Wnck.Screen.get_default()
        scr.force_update()
        win = scr.get_windows()
        list1=[]
        for window in  win:
            mywin=window.get_name()
            list1.append(window.get_name())
            str1 = "   " .join(name for name in list1 if  name not in 'panelx.py' )
            self.tool.setText(str1)
        Timer(1,self.panel).start()

    def closeEvent(self, event):
        event.ignore()
def main():
    app = QApplication(sys.argv)
    ex = Panel()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()


