#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_02_box_layout.py
@time: 2022/5/10  10:02
# @describe: PyQt6 QHBoxLayout

QHBoxLayout 和 QVBoxLayout 是基本的布局类，用于水平和垂直地排列小部件。

假设我们想在右下角放置两个按钮。为了创建这样的布局，我们使用一个水平框和一个垂直框。
为了创造必要的空间，我们添加了一个“拉伸因子”。

"""
import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication


class Example(QWidget):
    """ 窗口的右下角有两个按钮。当我们调整应用程序窗口的大小时，它们仍然在那里。
        这里使用了 HBoxLayout 和 QVBoxLayout。"""
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        ok_button = QPushButton('OK')
        cancel_button = QPushButton('Cancel')

        # 这里创建两个按钮
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(ok_button)
        hbox.addWidget(cancel_button)

        # 创建一个水平框布局，并添加一个拉伸因子和两个按钮。
        # 拉伸在两个按钮之前增加了一个可拉伸的空间，这将把他们推到窗口的右边
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 水平布局被放入垂直布局中。垂直框中的拉伸因子将把带有按钮的水平框推到窗口的底部。
        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())




