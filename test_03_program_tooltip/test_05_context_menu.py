#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_05_context_menu.py
@time: 2022/5/9  11:05
# @describe: PyQt6 上下文菜单-
    重新实现 contextMenuEvent 方法，调出一个上下文菜单。
    鼠标右击后，出现 New、Open、Quit

"""
import sys
from PyQt6.QtWidgets import QMainWindow, QMenu, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Context menu')
        self.show()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        openAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        # 使用 exec 方法调出上下文菜单，通过鼠标事件对象获得鼠标坐标点，
        # 再调用 mapToGlobal 方法把组件的坐标设置成全局的屏幕坐标。
        action = cmenu.exec(self.mapToGlobal(event.pos()))

        # 如果上下文菜单触发的动作是退出动作，就终止程序
        if action == quitAct:
            QApplication.instance().quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
