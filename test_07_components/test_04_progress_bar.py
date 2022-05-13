#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_04_progress_bar.py
@time: 2022/5/11  14:02
# @describe: PyQt6 QProgressBar

进度条是一个用于处理冗长任务的小部件。
它是动态的，以便用户知道任务正在进行中。QProgressBar 小部件在 PyQt6 工具包中提供了一个水平或垂直的进度条。
可以设置进度条的最小值和最大值，默认值为0和99。

"""
from PyQt6.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication, Qt
from PyQt6.QtCore import QBasicTimer
import sys


class Example(QWidget):
    """ 示例中，有一个水平进度条和一个按钮，点击按钮可以启动和停止进度条。 """
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        # 这是 QProgressBar 的构造器
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.do_action)

        self.pb.setOrientation(Qt.Horizontal)

        # 使用定时器对象启动进度条
        self.timer = QBasicTimer()
        self.step = 0
        self.pb.setFormat("%v")

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self, e):
        # 每个QObject 和它的后代都有一个 timerEvent 事件处理器，这里实现一些函数处理这些事件
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def do_action(self):
        # 在 doAction 方法里，处理定时器的开启和暂停
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            # 调用定时器的开始方法，触发定时器事件。方法有两个参数，超时时间和接收事件的对象
            self.timer.start(100, self)
            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())





