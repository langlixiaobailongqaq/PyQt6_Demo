#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_01_absolute_positioning.py
@time: 2022/5/10  09:46
# @describe: PyQt6 的布局管理-绝对定位

    布局管理是我们在应用程序窗口中放置小部件的方式。我们可以使用绝对定位或布局类来放置小部件。
    使用布局管理器管理布局是组织小部件的首选方法。

绝对定位：
    以像素为单位指定每个小部件的位置和大小。在使用绝对定位时，我们必须了解以下局限性:

    -如果我们调整窗口大小，窗口小部件的大小和位置不会改变
    -应用程序在不同的平台上看起来可能不同，改变应用程序的字体可能会破坏布局
    -如果要改变布局，我们必须完全重做我们的布局，这很繁琐耗时

我们使用 move 方法来定位小部件。在本例中也就是标签。
我们通过提供x和y坐标来定位。坐标系的起始点在左上角，x值从左到右递增。y值从上到下递增
"""
import sys
from PyQt6.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        lbl1 = QLabel('ZetCode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Absolute')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

