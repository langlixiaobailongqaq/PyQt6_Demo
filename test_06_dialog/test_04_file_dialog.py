#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_04_file_dialog.py
@time: 2022/5/11  10:08
# @describe: PyQt6 QFileDialog - 选择文件或者文件夹的对话框，可以用作选择或者保存操作
"""
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QFileDialog, QApplication
from PyQt6.QtGui import QIcon, QAction
from pathlib import Path
import sys


class Example(QMainWindow):
    """ 该示例有一个有居中显示的文本编辑部件的菜单栏和一个状态栏.
    菜单项显示了用于选择文件的 QFileDialog。文件的内容被加载到文本编辑小部件中。

    """
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.statusBar()

        open_file = QAction(QIcon('../open.png'), 'Open', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('Open new File')
        open_file.triggered.connect(self.show_dialog)

        menubar = self.menuBar()
        # Mac OS 对待菜单栏有些不同
        menubar.setNativeMenuBar(False)
        file_menu = menubar.addMenu('File')
        file_menu.addAction(open_file)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('File dialong')
        self.show()

    def show_dialog(self):
        # 这里弹出 QFileDialog。getOpenFileName 的第一个参数字符串是标题，第二个字符串指定对话框工作目录。
        # 我们使用 path 模块来确定用户的主目录。默认情况下，文件过滤器设置为所有文件 (*)。
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        # 读取选择文件并把内容放置到文本编辑部件里
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.text_edit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())