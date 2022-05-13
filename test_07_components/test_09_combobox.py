#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_09_combobox.py
@time: 2022/5/13  16:51
# @describe: PyQt6 QComboBox

QComboBox 是下拉选框组件，能让用户在一系列选项中进行选择。

"""
import sys
from PyQt6.QtWidgets import QWidget, QLabel, QComboBox, QApplication


class Example(QWidget):
    """ 示例中有一个 QComboBox 和一个 QLabel。
        下拉选框有一个包含五个选项的列表，是Linux发行版的名称。标签组件显示组合框中选择的选项。
     """
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel('Ubuntu', self)
        # 创建有五个选项的 QComboBox 组件。
        combo = QComboBox(self)

        combo.addItem('Ubuntu')
        combo.addItem('Mandriva')
        combo.addItem('Fedora')
        combo.addItem('Arch')
        combo.addItem('Gentoo')

        combo.move(50, 50)
        self.lbl.move(50, 150)
        # 如果选择了一个选项，就调用 onActivated 方法
        combo.textActivated[str].connect(self.on_activated)

        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('QComboBox')
        self.show()

    def on_activated(self, text):
        # 在这个方法里，设置选中的文本到标签组件里，然后调整标签组件大小
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())