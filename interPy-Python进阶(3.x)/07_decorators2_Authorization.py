#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 07_decorators2_Authorization.py
# Author        : huangkeke
# Time          : 2018/6/6 12:02
# Contact       : hkkhuang@163.com
# Description	: 装饰器使用场景-授权 Authorization
from functools import wraps


def requires_auth(f):
    @wraps()
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.name, auth.password)
            authenticate()
        return f(*args, **kwargs)
    return decorated

