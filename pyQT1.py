# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:09:46 2020

@author: My Laptop
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
 
def update():
    print("Take Off")


counter = 0

def TO_command():
    label_cond.setText("Take Off")
    
def LD_command():
    label_cond.setText("Landing")

def counter():
    label_counter.setText(str(counter))
        
app = QApplication(sys.argv)
win = QMainWindow()

width = 750
height= 750

win.setGeometry(100,100,width,height)
win.setWindowTitle("ROS GUI")
 
label = QtWidgets.QLabel(win)
label.setText("ROS Controller with PyQT5")
label.adjustSize()
label.move(275, 20)
 
label_cond = QtWidgets.QLabel(win)
label_cond.setText("Ready for Command")
label_cond.adjustSize()
label_cond.move(275, 200)

label_counter = QtWidgets.QLabel(win)
label_counter.setText(str(counter))
label_counter.adjustSize()
label_counter.move(275, 450)

TO_loc = (200, 375)
TO_button = QtWidgets.QPushButton(win)
TO_button.clicked.connect(TO_command)
TO_button.setText("Take Off")
TO_button.move(TO_loc[0], TO_loc[1])

LD_button = QtWidgets.QPushButton(win)
LD_button.clicked.connect(LD_command)
LD_button.setText("Landing")
LD_button.move(TO_loc[0] + 200, TO_loc[1])

counter_button = QtWidgets.QPushButton(win)
counter_button.clicked.connect(counter)
counter_button.setText("Counter")
counter_button.move(TO_loc[0], TO_loc[1] + 200)

win.show()
sys.exit(app.exec_())
