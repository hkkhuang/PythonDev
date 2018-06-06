#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 07_decorators1_first2.py
# Author        : huangkeke
# Time          : 2018/6/6 12:59
# Contact       : hkkhuang@163.com
# Description	:
from functools import wraps


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return 'function will not run'
        return f(*args, **kwargs)
    return decorated


@decorator_name
def func():
    return 'function is running'


can_run = True
print(func())

can_run = False
print(func())

"""
注意： @wraps接受⼀个函数来进⾏装饰， 并加⼊了复制函数名称、 注释⽂档、 参数列表等等的功能。
       这可以让我们在装饰器⾥⾯访问在装饰之前的函数的属性。
"""