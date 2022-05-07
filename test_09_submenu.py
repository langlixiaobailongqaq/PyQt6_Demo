#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_09_submenu.py
@time: 2022/5/7  17:49
# @describe: PyQt6 子菜单
"""
import sys
from PyQt6.QtWidgets import QMainWindow, QMenu, QApplication
from PyQt6.QtGui import QAction


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        # 使用 QMenu 创建一个新菜单。
        fileMenu = menubar.addMenu('File')

        # 使用addAction 给子菜单添加行为
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Submenu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())