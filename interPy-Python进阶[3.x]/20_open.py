#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 20_open.py
# Author        : huangkeke
# Time          : 2018/6/19 20:52
# Contact       : hkkhuang@163.com
# Description	: open函数


# 错误写法
def open_file():  # open的返回值是一个文件句柄
    f = open('photo.jpg', 'r+')
    jpgdata = f.read()
    f.close()  # 显示的调用close()函数关闭 前提是read()成功，如果在f=open(...)之后出现异常，f.close()不会被调用


# 正确写法
def open_file_right():
    with open('photo.jpg', 'r+') as f:  # 为了确保不管是否出现异常，文件都能关闭，将其包装成一个with语句
        jpgdata = f.read()


"""
# open的第⼀个参数是⽂件名。 第⼆个(mode 打开模式)决定了这个⽂件如何被打开。
读取⽂件， 传⼊r
读取并写⼊⽂件， 传⼊r+
覆盖写⼊⽂件， 传⼊w
在⽂件末尾附加内容， 传⼊a

⼀般来说， 如果⽂件格式是由⼈写的， 更可能是⽂本模式。
 jpg图像⽂件⼀般不是⼈写的（其实不是⼈直接可读的）， 应该以⼆进制模式来打开它们， ⽅法是在mode字符串后加⼀个b

如果你以⽂本模式打开⼀些东西（⽐如， 加⼀个t,或者就⽤r/r+/w/a） ， 你还必须知道要使⽤哪种编码。
在Pyhon 2.x版本⾥， open不⽀持显⽰地指定编码

io.open函数在Python 2.x中和3.x(是open的别名)中都有提供.可以传⼊encoding这个关键字参数来传⼊编码。

如果不传⼊任意编码， ⼀个系统-以及Python -指定的默认选项将被选中。
但这个默认选项经常是错误的， 或者默认编码实际上不能表达⽂件⾥的所有字符（经常发⽣在Python 2.x和/或Windows）
"""

"""
怎么找出正在读的⽂件是⽤哪种编码写的呢？ 
并没有⼀个⼗分简单的⽅式来检测编码。 
在不同的编码中， 同样的字节可以表⽰不同， 但同样有效的字符。
因此， 必须依赖⼀个元数据（⽐如， 在HTTP头信息⾥） 来找出编码。 
通常，⽂件格式将编码定义成UTF-8。
"""

# 读取⼀个⽂件， 检测它是否是JPG
import io

with open('photo.jpg', 'rb') as inf:
    jpgdata = inf.read()

if jpgdata.startswith(b'\xFF\xD8'):
    text = u'This is a JPEG file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

with io.open('summary.txt', 'w', encoding='utf-8')as outf:
    outf.write(text % len(jpgdata))
