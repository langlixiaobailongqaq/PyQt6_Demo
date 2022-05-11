#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_01_qinput_dialog.py
@time: 2022/5/10  14:39
# @describe: PyQt6 的对话框- QInputDialog
    QInputDialog 提供了一个简单方便的对话框来从用户那里获取输入。输入值可以是字符串、数字或列表中的项目。

"""
from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication
import sys


class Example(QWidget):
    """
    这个示例有一个按钮和行内编辑部件，按钮打开输入一个对话框，对话框里有一个文本输入框，
    用户输入的文本会显示在行内编辑部件里。
    """
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.show_dialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Input dialog')
        self.show()

    def show_dialog(self):
        # 这行代码打开了输入对话框，第一个参数是对话框标题，第二个参数是对话框里的提示信息。
        # 对话框会返回输入的文本和一个布尔值。如果点击 OK 按钮，这个布尔值是 true。
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            # 使用 setText() 从对话框里获取输入的文本。
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())