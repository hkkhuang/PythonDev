#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 14_introspection.py
# Author        : huangkeke
# Time          : 2018/6/11 8:37
# Contact       : hkkhuang@163.com
# Description	: 对象自省

# ⾃省(introspection)， 在计算机编程领域⾥， 是指在运⾏时来判断⼀个对象的类型的能⼒。它是Python的强项之⼀。

# ***************************************************************************************************************
# dir
# 返回⼀个列表， 列出了⼀个对象所拥有的属性和方法
my_list = [1, 2, 3]
print(dir(my_list))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
#  '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
#  '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
#  'reverse', 'sort']

# 上⾯的⾃省给了我们⼀个列表对象的所有⽅法的名字。 当你没法回忆起⼀个⽅法的名字，这会⾮常有帮助。
# 如果我们运⾏dir()⽽不传⼊参数， 那么它会返回当前作⽤域的所有名字。

# *****************************************************************************************************************
# type和id
# type()函数返回一个对象的类型
print(type(''))
# <class 'str'>

print(type([]))
# <class 'list'>

print(type({}))
# <class 'dict'>

print(type(dict))
# <class 'type'>


# id()函数返回任意不同种类对象的唯一ID
name = 'hkkhuang'
print(id(name))
# output: 1798978955312

# *****************************************************************************************************************
# inspect模块
# inspect模块提供许多有用的函数，来获取活跃对象的信息
# 如查看一个对象的成员
import inspect

print(inspect.getmembers(str))
"""
[('__add__', <slot wrapper '__add__' of 'str' objects>), ('__class__', <class 'type'>), 
('__contains__', <slot wrapper '__contains__' of 'str' objects>), 
('__delattr__', <slot wrapper '__delattr__' of 'object' objects>), 
('__dir__', <method '__dir__' of 'object' objects>), 
......
......
"""

