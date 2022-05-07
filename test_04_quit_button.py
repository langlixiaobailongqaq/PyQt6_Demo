#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_04_quit_button.py
@time: 2022/5/7  14:30
# @describe: PyQt6-退出按钮：QPushButton
"""
import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication


class Example(QWidget):
    def __init__(self):
        # 含义：单继承，即只有一个父类
        # 作用：执⾏⽗类的构造函数，使得我们能够调⽤⽗类的属性
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建了一个按钮，它是 QPushButton 类的一个实例。
        # 构造函数的第一个参数是按钮的标签。 第二个参数是父级小部件。父小部件是 Example 小部件，它继承自 QWidget。
        qbtn = QPushButton('Quit', self)
        # PyQt6 的事件处理系统是由信号和插槽机制构成的，点击按钮（事件），会发出点击信号。
        # 事件处理插槽可以是 Qt 自带的插槽，也可以是普通 Python 函数
        #
        # 使用 QApplication.instance 获取的 QCoreApplication 对象包含主事件循环————它处理和分派所有事件。
        # 单击的信号连接到终止应用程序的退出方法。 通信是在两个对象之间完成的：发送者和接收者。
        # 发送者是按钮，接收者是应用程序对象
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())