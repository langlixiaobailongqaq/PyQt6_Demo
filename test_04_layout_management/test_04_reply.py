#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_04_reply.py
@time: 2022/5/10  10:44
# @describe:  PyQt6- 示例：回复
"""
import sys
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication


class Example(QWidget):
    """   窗口里有三个标签，两个行编辑器和一个文本编辑组件，布局使用了 QGridLayout。"""
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        title_edit = QLineEdit()
        author_edit = QLineEdit()
        review_edit = QTextEdit()

        # 创建一个格栅布局，并设置了组件间的分割空间。
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(title_edit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(author_edit, 2, 1)

        grid.addWidget(review, 3, 0)
        # 如果需要往格栅里添加组件，指定组件的跨行和跨列的个数。本例，reviewEdit 组件占用了5行。
        grid.addWidget(review_edit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())