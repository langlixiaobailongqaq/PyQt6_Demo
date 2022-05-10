#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_03_calculator.py
@time: 2022/5/10  10:24
# @describe: PyQt6 QGridLayout
    QGridLayout 是最常用的布局类，它能把空间分为多行多列。

"""
import sys
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        # QGridLayout 实例创建了并把布局设置到窗口中。
        grid = QGridLayout()
        self.setLayout(grid)

        # 创建要用到的按钮上的标签。
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        # 创建了给格栅用到的位置
        positions = [(i, j) for i in range(5) for j in range(4)]

        # 创建了按钮，并用 addWidget 方法添加到布局里。
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


