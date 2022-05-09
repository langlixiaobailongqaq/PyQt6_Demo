#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_04_pop_ups.py
@time: 2022/5/7  15:35
# @describe: PyQt6-弹窗
"""
import sys
from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):
    """ 关闭 QWidget 操作会产生 QCloseEvent 事件。重新实现 closeEvent 事件处理，替换部件的默认行为。 """
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):
        # 这里创建了一个带有两个按钮的消息框：是和否。
        # 第一个参数是标题栏，第二个参数是对话框显示的消息文本，第三个参数是对话框中的按钮组合，最后一个参数是默认选中的按钮。
        # 返回值存储在变量 reply 中。
        reply = QMessageBox.question(self, 'Meassage', '你确定要退出吗？',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

