#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 17_lambda.py
# Author        : huangkeke
# Time          : 2018/6/13 21:58
# Contact       : hkkhuang@163.com
# Description	: lambda表达式

# lambda表达式是一行函数
# 在其他语言中称为匿名函数
# 不想在程序中对⼀个函数使⽤两次， 可以使⽤lambda表达式， 它们和普通的函数完全⼀样。

# 原型:
# lambda 参数：操作(参数)

# 示例
add = lambda x, y: x + y
print(add(3, 5))
# Output: 8

# 列表排序
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)
# output: [(13, -3), (4, 1), (1, 2), (9, 10)]
print()
