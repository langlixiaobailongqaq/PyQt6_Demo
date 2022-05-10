#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_04_event_object.py
@time: 2022/5/10  11:56
# @describe: PyQt6 事件对象
    事件对象是一个 Python object，包含了一系列描述这个事件的属性，具体内容要看触发的事件。


"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):
    """ 标签组件里，展示鼠标的坐标 """
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        x = 0
        y = 0
        self.text = f'x: {x}, y: {y}'

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignmentFlag.AlignTop)

        # 鼠标跟踪默认是关闭的，鼠标移动时，组件只能在鼠标按下的时候接收到事件。
        # 开启鼠标跟踪，只移动鼠标不按下鼠标按钮，也能接收到事件。
        self.setMouseTracking(True)
        self.setLayout(grid)

        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, e):
        # e 是事件对象，它包含了事件触发时候的数据。
        # 通过 position().x() 和 e.position().y() 方法，能获取到鼠标的坐标值
        x = int(e.position().x())
        y = int(e.position().y())

        text = f'x: {x}, y:{y}'
        self.label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())



