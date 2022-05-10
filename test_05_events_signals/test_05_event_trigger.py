#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_05_event_trigger.py
@time: 2022/5/10  13:56
# @describe: PyQt6 事件触发者
"""
import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):
    """ 本例中有两个按钮。 button_clicked 调用触发者方法确定了是哪个按钮触发的事件 """
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        btn1 = QPushButton("Button1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button2", self)
        btn2.move(150, 50)

        # 两个按钮绑定了同一个插槽
        btn1.clicked.connect(self.button_clicked)
        btn2.clicked.connect(self.button_clicked)

        self.statusBar()
        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Event sender')
        self.show()

    def button_clicked(self):
        # 在应用的状态栏里，显示了是哪个按钮被按下
        sender = self.sender()
        msg = f'{sender.text()} was pressed'
        self.statusBar().showMessage(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())