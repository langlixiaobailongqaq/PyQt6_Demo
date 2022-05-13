#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_08_splitter.py
@time: 2022/5/13  16:39
# @describe: PyQt6 QSplitter

QSplitter 允许用户通过拖动子部件之间的边界来控制子部件的大小
"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QFrame, QSplitter, QApplication


class Example(QWidget):
    """ 这里有三个 QFrame 组件和连个 QSplitter 组件，注意，在某些主题里，分割条可能不容易看到 """
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        hbox = QHBoxLayout(self)
        # 给框架组件设置一些样式，这样更容易看清楚边界
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.Shape.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.Shape.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.Shape.StyledPanel)

        # 创建一个有俩框架组件的 QSplitter 组件
        splitter1 = QSplitter(Qt.Orientation.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        # 再添加一个分割条和一个框架组件
        splitter2 = QSplitter(Qt.Orientation.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
