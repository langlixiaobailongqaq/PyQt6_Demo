#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_01_first_program.py
@time: 2022/5/7  13:58
# @describe: PyQt6 的第一个程序
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget


def main():
    # 每个 PyQt6 应用程序都必须创建一个应用程序对象。
    # sys.argv 参数是来自命令行的参数列表。Python 脚本可以从 shell 运行，这是应用启动的一种方式。
    app = QApplication(sys.argv)

    # QWidget 小部件是 PyQt6 中所有用户界面对象的基类。
    # 为 QWidget 提供了默认构造函数。默认构造函数没有父级。没有父级的小部件称为窗口。
    w = QWidget()
    # resize 方法改变了小部件的尺寸，现在它500像素宽，600像素高。
    w.resize(500, 600)
    # move 方法把小部件移动到屏幕的指定坐标(300, 300)。
    w.move(300, 300)

    # 使用 setWindowTitle 给窗口设置标题，标题显示在标题栏。
    w.setWindowTitle('Simple')
    # show 方法是在屏幕上显示小部件的方法。显示一个部件的步骤是首先在内存里创建，然后在屏幕上显示。
    w.show()

    # 最后，我们进入应用程序的主循环。事件处理从这里开始。
    # 主循环从窗口系统接收事件并将它们分派给应用程序小部件。
    # 如果我们调用 exit 方法或主小部件被销毁，则主循环结束。
    # sys.exit 方法确保一个干净的退出。环境将被告知应用程序如何结束。
    sys.exit(app.exec())


if __name__ == '__main__':
    main()