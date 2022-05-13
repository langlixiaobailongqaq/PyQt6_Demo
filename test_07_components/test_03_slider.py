#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_03_slider.py
@time: 2022/5/11  11:29
# @describe: PyQt6 QSlider

QSlider是一个有简单手柄的小部件，这个手柄可以前后拖动。通过这种方式，我们可以为特定的任务选择一个值。
有时使用滑块比输入数字或使用旋转框更自然。

"""
from PyQt6.QtWidgets import QWidget, QLabel, QSlider, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import sys


class Example(QWidget):
    """ 示例中，模拟了音量控制。通过拖动滑块的手柄，我们可以改变标签上的图像 """
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        # 创建一个水平的 QSlider
        sld = QSlider(Qt.Orientation.Horizontal, self)
        sld.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        sld.setGeometry(30, 40, 200, 30)
        # 把 valueChanged 信号和用户定义的 changeValue 方法绑定
        sld.valueChanged[int].connect(self.change_value)

        # 创建一个 QLabel 组件，并给它初始化一个静音的图标
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../mute.png'))
        self.label.setGeometry(250, 40, 80, 30)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QSlider')
        self.show()

    def change_value(self, value):
        # 根据滑块的值，修改标签的图像。在上面的代码中，
        # 如果滑块等于零，把标签改为mute.png图像(几个图片有点问题，懒得找了...问题不大)
        if value == 0:
            self.label.setPixmap(QPixmap('../mute.png'))
        elif 0 < value <= 30:
            self.label.setPixmap(QPixmap('../min.png'))
        elif 30 < value < 80:
            self.label.setPixmap(QPixmap('../med.png'))
        else:
            self.label.setPixmap(QPixmap('../max.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())