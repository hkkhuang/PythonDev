#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 16_exception.py
# Author        : huangkeke
# Time          : 2018/6/12 11:51
# Contact       : hkkhuang@163.com
# Description	: 异常处理

# 能触发异常产⽣的代码会放到try语句块⾥， ⽽处理异常的代码会在except语句块⾥实现。
# ***************************************************************************************************************
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
# output:
# An IOError occurred. No such file or directory

# ***************************************************************************************************************
# 处理多个异常
# 第⼀种⽅法需要把所有可能发⽣的异常放到⼀个元组⾥
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print('An error occurred.{}'.format(e.args[-1]))
# output:
# An error occurred.No such file or directory

# 另外⼀种⽅式是对每个单独的异常在单独的except语句块中处理
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print('An EOF error occurred.')
    raise e
except IOError as e:
    print('An IOError occurred.')
    raise e
# 如果异常没有被第⼀个except语句块处理， 那么它也许被下⼀个语句块处理， 或者根本不会被处理。

# 最后⼀种⽅式会捕获所有异常：
try:
    file = open('test.txt', 'rb')
except Exception:
    # 打印⼀些异常⽇志， 如果你想要的话
    raise
# 不知道程序会抛出什么样的异常时， 上⾯的可以捕获所有异常

# **************************************************************************************************************
# finally语句
# 主程序代码包裹进了try从句，把⼀些代码包裹进⼀个except从句， 会在try从句中的代码触发异常时执⾏。
# 包裹到finally从句中的代码不管异常是否触发都将会被执⾏。
# 这可以被⽤来在脚本执⾏之后做清理⼯作。
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print('This would be printed whether or not an exception occurred')

# **************************************************************************************************************
# try/else从句
# 在没有触发异常的时候执⾏⼀些代码。可以通过⼀个else从句来达到。
# 只是想让⼀些代码在没有触发异常的情况下执⾏， 为啥你不直接把代码放在try⾥⾯呢？
# 那样的话这段代码中的任意异常都还是会被try捕获， 不⼀定想要那样。
try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # 这⾥的代码只会在try语句⾥没有触发异常时运⾏,
    # 但是这⾥的异常将不会被捕获
    print('This would only run if no exception occurs. And an error here would NOT be caught.')
finally:
    print('This would be printed in every case.')

# else从句只会在没有异常的情况下执⾏， ⽽且它会在finally语句之前执⾏。
