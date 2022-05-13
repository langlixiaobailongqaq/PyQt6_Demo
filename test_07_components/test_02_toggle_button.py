#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_02_toggle_button.py
@time: 2022/5/11  11:09
# @describe: PyQt6-切换按钮

切换按钮是 QPushButton 的一个特殊情况。它有两个状态：按下与否，鼠标点击触发。

"""
from PyQt6.QtWidgets import QWidget, QPushButton, QFrame, QApplication
from PyQt6.QtGui import QColor
import sys


class Example(QWidget):
    """
    示例中，创建了三个切换按钮和一个 QWidget。并将 QWidget 的背景颜色设置为黑色。
    切换按钮用于切换颜色值为红色、绿色和蓝色。组件背景颜色取决于按下的按钮。

    """
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        # 初始化颜色为黑色
        self.col = QColor(0, 0, 0)
        # 创建一个 QPushButton 并调用 setCheckable 方法设为为可选，就创建了一个切换按钮
        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)

        # 把用户自定义的方法和点击信号绑定，用点击信号改变一个布尔值。
        redb.clicked[bool].connect(self.set_color)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)
        greenb.clicked[bool].connect(self.set_color)

        blueob = QPushButton('Blue', self)
        blueob.setCheckable(True)
        blueob.move(10, 110)
        blueob.clicked[bool].connect(self.set_color)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet('QWidget { background-color: %s }' %self.col.name())

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Toggle button')
        self.show()

    def set_color(self, pressed):
        # 获取到点击的按钮
        souce = self.sender()
        if pressed:
            val = 255
        else:
            val = 0
        # 如果点击的是红色按钮，就相应的把颜色改成红色
        if souce.text() == 'Red':
            self.col.setRed(val)
        elif souce.text() == 'Green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        # 使用样式表修改背景颜色，修改样式需要调用 setStyleSheet 方法
        self.square.setStyleSheet("QFrame { background-color: %s}" % self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())