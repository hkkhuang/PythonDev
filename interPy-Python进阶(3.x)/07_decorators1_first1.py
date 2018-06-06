#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 07_decorators1_first1.py
# Author        : huangkeke
# Time          : 2018/6/6 12:53
# Contact       : hkkhuang@163.com
# Description	:
from functools import wraps


def a_new_decorator(a_func):
    """
    定义装饰器
    :param a_func: 传递参数 函数
    :return:
    """

    @wraps(a_func)
    def wrap_the_function():
        print('I am doing some boring work before executing a_func()')
        a_func()
        print('I am doing some boring work after executing a_func()')

    return wrap_the_function


@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print('I am the function which needs some decoration to remove my foul smell')


a_function_requiring_decoration()
# output
# I am doing some boring work before executing a_func()
# I am the function which needs some decoration to remove my foul smell
# I am doing some boring work after executing a_func()

print(a_function_requiring_decoration.__name__)
# output
# a_function_requiring_decoration
