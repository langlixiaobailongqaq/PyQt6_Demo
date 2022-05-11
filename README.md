## 介绍
* 环境：mac + python3.8 + PyQt6-6.3.0

### 安装：
* pip install PyQt6

### 官方文档地址：
* https://www.riverbankcomputing.com/static/Docs/PyQt6/


## PYQt6 介绍
* Qt 是一组跨平台的 C++ 库，它们实现了用于访问现代桌面和移动系统的许多方面的高级 API。其中包括定位和定位服务、多媒体、NFC 和蓝牙连接、基于 Chromium 的网络浏览器以及传统的 UI 开发。


* PyQt6 是一套针对 Qt v6 的综合 Python 绑定。它被实现为超过 35 个扩展模块，使 Python 能够在所有支持的平台（包括 iOS 和 Android）上用作 C++ 的替代应用程序开发语言。


* PyQt6 也可以嵌入基于 C++ 的应用程序中，以允许这些应用程序的用户配置或增强这些应用程序的功能。


## PyQt6 组件
* PyQt6 包含许多不同的组件。首先，有许多 Python 扩展模块。这些都安装在 PyQt6Python 包中，并在 模块列表中进行了描述。


* 每个扩展模块都有一个对应的PEP 484定义的存根文件，其中包含模块 API 的类型提示。这可以由诸如 mypy 之类的静态类型检查器使用。


* PyQt6 包含允许使用 Python 代码扩展Qt Designer 和qmlscene的插件。有关详细信息，请分别参阅编写 Qt Designer 插件和 集成 Python 和 QML。


* PyQt6 还包含几个实用程序。


* pyuic6对应于 Qt uic实用程序。它将 使用 Qt Designer 创建的基于QtWidgets的 GUI 转换为 Python 代码。


* pylupdate6对应于 Qt lupdate实用程序。它从 Python 代码中提取所有可翻译的字符串并创建或更新.ts翻译文件。然后 Qt Linguist 使用这些来管理这些字符串的翻译。


* DBus支持模块安装为 dbus.mainloop.pyqt6 。dbus-python 该模块为 Qt 事件循环提供支持，就像标准绑定包中包含的 dbus.mainloop.glib 为 GLib 事件循环提供支持一样。DBus 支持中描述了 API 。仅当安装了dbus-python v0.80（或更高版本）绑定包时才可用。QtDBus 模块为 DBus 提供了更类似于 Qt 的接口。


* PyQt6 包含大量示例。这些是 Qt 提供的许多 C++ 示例的 Python 端口。它们可以在 examplessdist 的目录中找到。


* 最后，PyQt6 包含允许绑定其他基于 Qt 的类库的规范文件，这些类库进一步扩展了 PyQt6 的开发和安装。


## PyQt6 模块
* PyQt6 类是由一系列模块组成的，包括如下的模块：

  * QtCore：非GUI 的核心库。这个模块用来处理时间、文件、目录、各种类型的数据、流(stream)、URLs，mime类型、线程和进程。
  * QtGui：有窗口系统集成、事件处理、2D图形，基本图像、字体、文本的类。
  * QtWidgets：有创建经典风格的用户界面的类。
  * QtDBus: 使用 D-Bus 处理 IPC 通讯的类。
  * QtNetwork： 网络编程类，这些类使网络编程变得更容易，可移植性也更好，方便了 TCP/IP 和 UDP服务端和客户端编程。
  * QtHelp：包含了创建、查看和搜索文档的类。
  * QtXml：包含了处理XML 文件的类，实现了 SAX和 DOM API。
  * QtSvg：提供了显示 SVG的类，可缩放矢量图形(SVG)是一种描述二维图像和图像应用的XML语言。
  * QtSql：提供了数据库的类。
  * QtTest：提供了可以对 PyQt6 应用进行单元测试的工具。
  


## demo涉及知识点：
* PyQt6-日期和时间


* PyQt6-第一个程序：
  * PyQt6 简单示例
  * PyQt6 tooltip
  * PyQt6 退出按钮
  * PyQt6 弹窗
  * PyQt6 窗口居中
  

* PyQt6 的菜单和工具栏
  * PyQt6 状态栏
  * PyQt6 简单菜单
  * PyQt6 子菜单
  * PyQt6 勾选菜单
  * PyQt6 上下文菜单
  * PyQt6 工具栏
  * PyQt6 主窗口


* PyQt6 的布局管理
  * 绝对定位
  * PyQt6 QHBoxLayout
  * PyQt6 QGridLayout
  * 示例：回复


* PyQt6 的事件和信号
  * PyQt6 中的事件
  * PyQt6 信号和插槽
  * PyQt6 重新实现事件处理器
  * PyQt6 事件对象
  * PyQt6 事件触发者
  * PyQt6 触发信号


* PyQt6 的对话框
  * PyQt6 QInputDialog
  * PyQt6 QColorDialog
  * PyQt6 QFontDialog
  * PyQt6 QFileDialog


* PyQt6 组件


* PyQt6 的拖拽操作


* PyQt6 自定义部件


* PyQt6-俄罗斯方块