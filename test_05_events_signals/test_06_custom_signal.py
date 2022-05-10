#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_06_custom_signal.py
@time: 2022/5/10  14:17
# @describe: PyQt6 触发信号

QObject 可以主动触发信号。

"""
import sys
from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtWidgets import QMainWindow, QApplication


class Communication(QObject):
    """ 创建了一个叫 closeApp 的信号，在鼠标按下的时候触发，和关闭插槽 QMainWindow 绑定。 """
    close_app = pyqtSignal()


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        # 自定义信号 closeApp 绑定到 QMainWindow 的关闭插槽上。
        self.c = Communication()
        self.c.close_app.connect(self.close)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, e):
        # 在窗口上点击鼠标按钮的时候，触发 closeApp 信号，程序终止
        self.c.close_app.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())