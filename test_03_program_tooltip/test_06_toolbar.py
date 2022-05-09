#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_06_toolbar.py
@time: 2022/5/9  16:17
# @describe: PyQt6 工具栏-
    创建了一个简单的状态栏，只有一个行为，关闭应用
"""
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon, QAction


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 创建一个行为对象，对象有标签，图标和快捷键。然后把 QApplication 的退出方法和行为发出的信号绑定。
        exitAct = QAction(QIcon('../exit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(QApplication.instance().quit)

        # 使用 addToolBar 方法创建工具栏，然后使用 addAction 方法添加行为。
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
