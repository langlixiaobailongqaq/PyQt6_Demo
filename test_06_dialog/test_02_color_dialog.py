#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_02_color_dialog.py
@time: 2022/5/10  17:48
# @describe: PyQt6 QColorDialog-选择颜色对话框
"""
from PyQt6.QtWidgets import QWidget, QPushButton, QFrame, QColorDialog, QApplication
from PyQt6.QtGui import QColor
import sys


class Example(QWidget):
    """ 示例里有个按钮和一个 QFrame。部件的背景颜色是默认颜色，
        可以使用 QColorDialog 修改部件的背景颜色。

     """
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        # 这是 QFrame 的初始背景色。
        col = QColor(0, 0, 0)
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.show_dialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget {background-clor: %s}" % col.name())
        self.frm.setGeometry(130, 22, 200, 200)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Color dialog')
        self.show()

    def show_dialog(self):
        # 这一行弹出 QColorDialog
        col = QColorDialog.getColor()
        # 这里检查了颜色是不是有效的。如果点击取消按钮，没有返回可用的颜色值。
        # 如果返回的颜色是有效值，就使用样式表修改背景颜色。
        if col.isValid():
            self.frm.setStyleSheet("QWidget {background-color: %s}" %col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())