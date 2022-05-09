#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_04_check_menu.py
@time: 2022/5/9  10:21
# @describe: PyQt6 勾选菜单-
    创建只有一个行为的 View 菜单。这个行为用来展现或者隐藏状态栏，如果状态栏可见，菜单是勾选的状态。
"""
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QAction


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        # mac 记得加上 下面的一行代码
        menubar.setNativeMenuBar(False)
        viewMenu = menubar.addMenu('View')

        # 使用 checkable 参数创建一个可以勾选的菜单。
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        # 使用 checkable 参数创建一个可以勾选的菜单。
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggle_menu)

        viewMenu.addAction(viewStatAct)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Check menu')
        self.show()

    def toggle_menu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


