#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 07_decorators1_first.py
# Author        : huangkeke
# Time          : 2018/6/6 12:46
# Contact       : hkkhuang@163.com
# Description	: 第一个装饰器


def a_new_decorator(a_func):
    def wrap_the_function():
        print('I am doing some boring work before executing a_func()')
        a_func()
        print('I am doing some boring work after executing a_func()')
    return wrap_the_function


def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print('I am the function which needs some decoration to remove my foul smell')


a_function_requiring_decoration()
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()
print(a_function_requiring_decoration.__name__)  # wrap_the_function
