#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_05_calendar_widget.py
@time: 2022/5/12  16:30
# @describe: PyQt6 QCalendarWidget

QCalendarWidget 提供了一个月视图的日历组件，它能让用户简单直观的选择日期。

"""
from PyQt6.QtWidgets import QWidget, QCalendarWidget, QLabel, QApplication, QVBoxLayout
from PyQt6.QtCore import QDate
import sys


class Example(QWidget):
    """ 该示例有一个日历组件和一个标签组件，选择的日期显示在标签组件里 """
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout(self)
        # 创建了一个 QCalendarWidget
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        # 选中一个日期，会触发 clicked[QDate] 信号，信号是和用户定义的 showDate 方法绑定。
        cal.clicked[QDate].connect(self.show_date)

        vbox.addWidget(cal)
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def show_date(self, date):
        # 调用 selectedDate 方法获取到选中的日期，再把日期转换成字符串，设置到标签组件里
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())







