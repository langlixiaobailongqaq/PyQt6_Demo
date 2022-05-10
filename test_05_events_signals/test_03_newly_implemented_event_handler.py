#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_03_newly_implemented_event_handler.py
@time: 2022/5/10  11:45
# @describe: PyQt6 重新实现事件处理器

PyQt6里，事件的处理器一般都会重新实现。

译注：所有的事件处理器都有默认的实现，也就是默认事件。
默认事件可能有自己的逻辑，比如拖选，点击，有的可能只是一个空函数。
空函数都需要重新覆盖原来的实现，达到事件处理的目的。
有默认事件处理函数的，也有可能被覆盖实现，比如禁用自带的拖选，或者重写拖选的效果等。
"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Event handler')
        self.show()

    # 重新实现了 keyPressEvent 的事件处理器-按下 Escape 按钮，应用会退出。
    def keyPressEvent(self, e):
        if e.key() == Qt.key.Key_Escape.value:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

