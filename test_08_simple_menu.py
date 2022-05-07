#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_08_simple_menu.py
@time: 2022/5/7  16:39
# @describe:  PyQt6 简单菜单
"""

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon, QAction


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        """
        QAction 是行为抽象类，包括菜单栏，工具栏，或自定义键盘快捷方式。
        下面的三行中，创建了一个带有特定图标和 'Exit' 标签的行为。
        此外，还为该行为定义了一个快捷方式。第三行创建一个状态提示，
        当我们将鼠标指针悬停在菜单项上时，状态栏中就会显示这个提示。
        :return:
        """
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        # 当选择指定的行为时，触发了一个信号，这个信号连接了 QApplication 组件的退出操作，这会终止这个应用程序
        exitAct.triggered.connect(QApplication.instance().quit)

        # menuBar 方法创建了一个菜单栏，然后使用 addMenu 创建一个文件菜单，使用 addAction 创建一个行为。
        self.statusBar()
        menubar = self.menuBar()
        # Mac OS 对待菜单栏有些不同。为了获得全平台一致的效果，
        # 我们可以在代码中加入一行：menubar.setNativeMenuBar(False)。
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('simple menu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())