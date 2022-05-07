#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: test_01_data_time.py
@time: 2022/5/7  10:40
# @describe: PyQt6-日期和时间：QDate,QTime,QDateTime
"""

"""
1. PyQt6 有 QDate, QDateTime, QTime 类处理日期和时间。
    QDate 是用于处理公历中的日期的类。它有获取、比较或操作日期的方法。
    QTime 类用于处理时间。它提供了比较时间、确定时间和其他各种时间操作方法。
    QDateTime 是 QDate 和 QTime 的组合。
    
2.PyQt6 有 currentDate、currentTime 和 currentDateTime 方法获取当前的日期或时间。

3.PyQt6 UTC 时间: toUTC()

4.PyQt6 天数：
    daysInMonth：返回指定月份的天数
    daysInYear：返回指定年份的天数
    daysTo：返回一个日期到另外一个日期的差
    
5.PyQt6 夏令时：
    夏令时 (DST) 是在夏季调快时间，使晚上变得更长。 初春时调前调一小时，秋季时调后调至标准时间。

6.PyQt6 unix 纪元：
    纪元是被选为特定纪元起源的时间瞬间。 例如，在西方基督教国家，时间纪元从耶稣诞生的第 0 天开始。 另一个例子是使用了十二年的法国共和历。 
    这个时代是共和时代的开始，1792 年 9 月 22 日宣布第一共和国成立，君主制也被废除。

    计算机也有它的时代。 最受欢迎的时代之一是 Unix 时代。
    Unix 纪元是 1970 年 1 月 1 日 UTC 时间 00:00:00（或 1970-01-01T00:00:00Z ISO 8601）。 
    计算机中的日期和时间是根据自该计算机或平台定义的纪元以来经过的秒数或时钟滴答数确定的。
    
7.PyQt6 Julian day-儒略日:
    a.儒略日是指自儒略时期开始以来的连续天数。 它主要由天文学家使用。 它不应与儒略历混淆。 
    b.它开始于公元前 4713 年。第 0 天是公元前 4713 年 1 月 1 日中午的那天。

    c.儒略日数 (JDN) 是自此期间开始以来经过的天数。 任何时刻的儒略日期 (JD) 是前一个中午的儒略日数加上自该时刻起当天的分数。
     （Qt 不计算这个分数。）除了天文学，儒略日期经常被军事和大型机程序使用
     
    d.使用儒略日可以进行跨越几个世纪的计算。

"""

from PyQt6.QtCore import QDate, QTime, QDateTime, Qt

""" 获取当前的日期或时间 """
# currentDate: 返回当前的日期
now = QDate.currentDate()
# 获取不同格式的日期
print(now.toString(Qt.DateFormat.ISODate))
print(now.toString(Qt.DateFormat.RFC2822Date))

# 返回当前的日期和时间
datetime = QDateTime.currentDateTime()
print(datetime.toString())

# 返回当前的时间
time = QTime.currentTime()
print(time.toString(Qt.DateFormat.ISODate))


""" PyQt6-UTC时间-currentDateTime:返回本地时间的当前时间 """
now = QDateTime.currentDateTime()
print('本地日期时间', now.toString(Qt.DateFormat.ISODate))
# toUTC：从时间对象里获取标准时间
print('通用日期时间', now.toUTC().toString(Qt.DateFormat.ISODate))
# offsetFromUtc：本地时间与标准时间的差，以秒为单位
print(f'与 UTC 的差: {now.offsetFromUtc()} 秒')
print('本地日期时间:', now.toString(Qt.DateFormat.ISODate))


""" PyQt6 天数 """
now = QDate.currentDate()
d = QDate(2022, 5, 7)
print(f'月的天数: {d.daysInMonth()}')
print(f'年中的天数: {d.daysInYear()}')


""" PyQt6 天数差 """
now = QDate.currentDate()
y = now.year()
print(f'today is {now.toString(Qt.DateFormat.ISODate)}')

xmas1 = QDate(y-1, 12, 25)
xmas2 = QDate(y, 5, 8)
dayspadded = xmas1.daysTo(now)
print(f'{dayspadded} 自去年圣诞节以来已经过去了几天')

nofdays = now.daysTo(xmas2)
print(f'距离指定日期还有 {nofdays} 天')


""" PyQt6 时间的计算 """
now = QDateTime.currentDateTime()
print(f'今天: {now.toString(Qt.DateFormat.ISODate)}')
print(f'增加 12 天: {now.addDays(12).toString(Qt.DateFormat.ISODate)}')
print(f'减去 12 天: {now.addDays(-12).toString(Qt.DateFormat.ISODate)}')

print(f'增加50秒: {now.addSecs(50).toString(Qt.DateFormat.ISODate)}')
print(f'增加3个月: {now.addMonths(3).toString(Qt.DateFormat.ISODate)}')
print(f'增加3年: {now.addYears(3).toString(Qt.DateFormat.ISODate)}')


""" PyQt6 夏令时 """
now = QDateTime.currentDateTime()
print(f'时区： {now.timeZoneAbbreviation()}')
if now.isDaylightTime():
    print('当前日期属于 DST 时间')
else:
    print('当前日期不属于 DST 时间')


""" PyQt6- unix 纪元 """
# 获取当前的日期和时间
now = QDateTime.currentDateTime()
# toSecsSinceEpoch 返回 Unix 时间
unix_time = now.toSecsSinceEpoch()
print(unix_time)

# fromSecsSinceEpoch 方法把 Unix 时间转换成 QDateTime
d = QDateTime.fromSecsSinceEpoch(unix_time)
print(d.toString(Qt.DateFormat.ISODate))


""" PyQt6- Julian day"""
now = QDate.currentDate()
print('今天的公历日期', now.toString(Qt.DateFormat.ISODate))
print('儒略日的日期', now.toJulianDay())


""" PyQt6-历史战役-使用儒略日可以进行跨越几个世纪的计算 """
borodino_battle = QDate(1812, 9, 7)
slavkov_battle = QDate(1805, 12, 2)
print('两个拿破仑战斗日期:', borodino_battle, slavkov_battle)
now = QDate.currentDate()

j_today = now.toJulianDay()
j_borodino = borodino_battle.toJulianDay()
j_slavkov = slavkov_battle.toJulianDay()
print('今天以及斯拉夫科夫和博罗季诺战役的儒略日', j_today, j_borodino, j_slavkov)

day1 = j_today - j_slavkov
day2 = j_today - j_slavkov
print('两次大战的天数差', day1, day2)