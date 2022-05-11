#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_03_font_dialog.py
@time: 2022/5/11  09:52
# @describe: PyQt6 QFontDialog-选择字体的对话框
"""
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QLabel, QFontDialog, QApplication
import sys


class Example(QWidget):
    """ 本例中，有个有文本的按钮。使用 QFontDialog 可以修改按钮文本的字体。 """
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        btn.move(20, 20)

        vbox.addWidget(btn)
        btn.clicked.connect(self.show_dialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Font dialong')
        self.show()

    def show_dialog(self):
        # 这里弹出了字体选择对话框。getFont 方法返回了选择的字体名称和 ok 参数，
        # 如果点击 Ok 按钮，ok 的值是 True，反则是 False。
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())