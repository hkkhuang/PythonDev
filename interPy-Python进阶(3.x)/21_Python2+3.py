#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 21_Python2+3.py
# Author        : huangkeke
# Time          : 2018/6/20 9:32
# Contact       : hkkhuang@163.com
# Description	: 兼容Python2+3

# 同时兼容Python2和Python3
# *******************************************************************************************************************
# 第⼀种也是最重要的⽅法， 就是导⼊__future__模块。 可以在Python2中导⼊Python3的功能。

# 上下⽂管理器是Python2.6+引⼊的新特性， 如果在Python2.5中使⽤它可以这样做:
from __future__ import with_statement


# 在Python3中print已经变为⼀个函数。 如果在Python2中使⽤它可以通过__future__导⼊：
from __future__ import print_function
print(print)
# output: <built-in function print>

# *******************************************************************************************************************
# 模块重命名
# 在脚本中导⼊模块,⼤多时候我们会这样做：
import foo
# 或者
from foo import bar

 # 其实你也可以这样做：
import foo as foo

try:
    import urllib.request as urllib_request    # for python3
except ImportError:
    import urllib2 as urllib_request  # for python2

# 将模块导⼊代码包装在try/except语句中。
# 是因为在Python2中并没有urllib.request模块,这将引起⼀个ImportError异常。
# 在Python2中urllib.request的功能则是由urllib2提供。
# 所以, 当我们试图在Python2中导⼊urllib.request模块的时候， ⼀旦我们捕获到ImportError我们将通过导⼊urllib2模块来代替它。

# as关键字的作⽤--将导⼊的模块映射到urllib.request，通过urllib_request这个别名可以使⽤urllib2中的所有类和⽅法。

# *******************************************************************************************************************
# 过期的Python2内置功能
# Python2中有12个内置功能在Python3中已经被移除了。 要确保在Python2代码中不要出现这些功能来保证对Python3的兼容。
# ⼀个强制让你放弃12内置功能的⽅法：
from future.builtins.disabled import *

# 只要尝试在Python3中使⽤这些被遗弃的模块时， 就会抛出⼀个NameError异常
apply()
# Output: NameError: obsolete Python 2 builtin apply is disabled