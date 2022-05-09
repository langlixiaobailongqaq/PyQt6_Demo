#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_02_first_program_tooltip.py
@time: 2022/5/7  14:10
# @describe: PyQt6 tooltip-气泡提示
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt6.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 气泡提示框设置了字体，这里使用了10pt 的 SansSerif 字体。
        QToolTip.setFont(QFont('SansSerif', 10))
        # 调用 setTooltip 方法创建气泡提示框，可以使用富文本内容。
        self.setToolTip('我是气泡')

        # 在气泡提示框上添加了一个按钮部件。
        btn = QPushButton('Button', self)
        btn.setToolTip('我是气泡啊')
        # sizeHint 方法是给按钮一个系统建议的尺寸
        btn.resize(btn.sizeHint())
        # 使用 move 方法移动这个按钮的位置。
        btn.move(50, 50)

        # setGeometry 四个参数: x坐标、y纵坐标、 宽、 高(坐标从屏幕左上角开始)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())