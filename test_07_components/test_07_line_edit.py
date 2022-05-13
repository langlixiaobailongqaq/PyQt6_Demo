#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_07_line_edit.py
@time: 2022/5/13  16:24
# @describe: PyQt6 QLineEdit

QLineEdit是一个可以输入单行文本的组件，它有撤消和重做、剪切和粘贴以及拖放功能。

"""
import sys
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QApplication


class Example(QWidget):
    """ 本例中有一个 QLineEdit 组件和一个标签，在编辑器里输入的文本会立即显示在标签里 """
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel(self)
        # 创建一个 QLineEdit 组件
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)

        # 如果编辑器的文本发生了变化，就调用 onChanged 方法
        qle.textChanged[str].connect(self.on_changed)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QLineEdit')
        self.show()

    def on_changed(self, text):
        # 在 onChanged 里，把输入的文本设置到标签组件里，同时使用 adjustSize 方法调整文字显示
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

