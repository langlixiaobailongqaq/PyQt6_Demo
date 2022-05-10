#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_02_signals_slots.py
@time: 2022/5/10  11:25
# @describe: PyQt6 信号和插槽
"""
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication


class Example(QWidget):
    """ 本例中，展示了 QtGui.QLCDNumber 和 QtGui.QSlider。我们可以通过拖动滑块改变显示器里的数字 """
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Orientation.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        # 把滑块的 valueChanged 事件和 显示器 display 插槽绑定到一起。
        # sender 是触发信号的对象， receiver 是接收信号的对象，slot 是对信号做出反应的方法。
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Signal and slot')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())