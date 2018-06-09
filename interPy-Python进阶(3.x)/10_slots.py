#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 10_slots.py
# Author        : huangkeke
# Time          : 2018/6/8 14:42
# Contact       : hkkhuang@163.com
# Description	: __slots__魔法

# 在Python中， 每个类都有实例属性。
# 默认情况下Python⽤⼀个字典来保存⼀个对象的实例属性。,它允许我们在运⾏时去设置任意的新属性。

# 然而对于已知属性的小类来说，这种特性可能是一瓶颈，因为这个字典浪费了很多内存，
# Python不那个跟在对象创建的时候直接分配一个固定的内存来保存所有的属性，当创建很多对象的时候会消耗很多内存

# 有一个方法来规避这个问题，就是使用__slots__ 来告诉Python不要使用字典，而且只给一个固定集合的属性分配空间


# 不使用slots
class MyClass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()


# 使用slots
 # 第⼆段代码会为你的内存减轻负担。 通过这个技巧， 有些⼈已经看到内存占⽤率⼏乎40%~50%的减少。
class MyClass(object):
    __slots__ = ['name', 'identifier']

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()

