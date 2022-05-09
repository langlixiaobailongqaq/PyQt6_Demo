#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_05_win_center.py
@time: 2022/5/7  15:52
# @describe: PyQt6-窗口居中
"""
import sys
from PyQt6.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.iniUI()

    def iniUI(self):
        # 设置窗口大小
        self.resize(350, 250)
        # 使用自定义 center 方法居中显示窗口。
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        # 得到一个矩形的窗口，这里可以放置所有类型的窗口
        qr = self.frameGeometry()
        # 屏幕属性里计算出分辨率，然后计算出中心点位置
        cp = self.screen().availableGeometry().center()

        # 把矩形窗口的中心点放置到屏幕窗口的中心点
        qr.moveCenter(cp)
        # 把应用窗口的左上方点坐标移动到矩形窗口的左上方，这样就可以居中显示了。
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())