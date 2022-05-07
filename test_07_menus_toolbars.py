#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_07_menus_toolbars.py
@time: 2022/5/7  16:18
# @describe: PyQt6 的菜单和工具栏

1. PyQt6 QMainWindow：
    QMainWindow 类提供了主程序窗口。在这里可以创建一个具有状态栏、工具栏和菜单栏的经典应用程序框架。

"""

""" PyQt6 状态栏 """
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 使用 QtGui.QMainWindow 方法创建状态栏，该方法创建了一个状态栏，
        # 并返回statusbar对象，再调用 showMessage 方法在状态栏上显示一条消息。
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Statusbar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())