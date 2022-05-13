#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_06_pixmap.py
@time: 2022/5/13  16:10
# @describe: PyQt6 QPixmap

QPixmap 是用于处理图像的小组件，为显示图像进行了优化
"""

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication
from PyQt6.QtGui import QPixmap
import sys


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        hbox = QHBoxLayout(self)
        # 用文件名作为参数创建一个 QPixmap 对象
        pixmap = QPixmap('../open.png')

        lbl = QLabel(self)
        # 然后把 pixmap 放到 QLabel 组件里
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Sid')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())