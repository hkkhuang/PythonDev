#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 13_enumerate.py
# Author        : huangkeke
# Time          : 2018/6/10 8:48
# Contact       : hkkhuang@163.com
# Description	: 枚举 enumerate

# 枚举是Python内置函数
# 遍历数据并⾃动计数
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

# output:
# 1 apple
# 2 banana
# 3 grapes
# 4 pear

# 上⾯这个可选参数允许我们定制从哪个数字开始枚举。
# 还可以⽤来创建包含索引的元组列表，
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# output:
# [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]
