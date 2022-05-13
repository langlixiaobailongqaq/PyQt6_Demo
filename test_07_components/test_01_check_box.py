#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_01_check_box.py
@time: 2022/5/11  10:48
# @describe: PyQt6 QCheckBox

组件是应用程序的基础组成部分。PyQt6 具有各种各样的小部件，包括按钮、复选框、滑块或列表框。

QCheckBox 组件有两个状态：选中和非选中。由个选框和文字组成，主要用于表示某个属性时开启还是关闭。
"""
from PyQt6.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt6.QtCore import Qt
import sys


class Example(QWidget):
    """ 创建了一个切换窗口标题的复选框。 """
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        # 这是 QCheckBox 构造器
        cb = QCheckBox('Show Title', self)
        cb.move(20, 30)
        # 设置了窗口标题，所以这里勾选上复选框
        cb.toggle()
        # 把用户定义的 changeTitle 方法和 stateChanged 信号连接起来。changeTitle 方法用来切换窗口标题
        cb.stateChanged.connect(self.change_title)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QCheckBox')
        self.show()

    def change_title(self, state):
        # 组件的状态是 changeTitle 方法改变变量得到的。如果选中组件，就设置窗口的标题。
        # 否则，标题栏是一个空字符串(或者指定显示的字符串)
        if state == Qt.CheckState.Checked.value:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('  ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
