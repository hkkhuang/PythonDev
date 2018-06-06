#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 07_decorators2_logging.py
# Author        : huangkeke
# Time          : 2018/6/6 13:06
# Contact       : hkkhuang@163.com
# Description	: 装饰器使用场景-日志 logging
from functools import wraps


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addtion_func(x):
    """Do some math"""
    return x + x


print(addtion_func(5))
