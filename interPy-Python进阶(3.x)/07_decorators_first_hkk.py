#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 07_decorators_first-1.py
# Author        : huangkeke
# Time          : 2018/6/5 14:06
# Contact       : hkkhuang@163.com
# Description	: 第⼀个装饰器
from functools import wraps
import logging

"""
简单地说： 装饰器是修改其他函数的功能的函数。

装饰器是一个函数，其主要用途是包装另一个函数或类。这种包装的首要目的是透明地修改或增强被包装对象的行为。

装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。装饰器是解决这类问题的绝佳设计，
有了装饰器，就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
"""

# 【示例1】******************************************************************************************************
# 开始我们有一个函数
# def fun1():
#     print("this is fun")


# 现在有新的需求，对这个函数增加一个记录日志功能
# 我们最直接方法在原来函数代码中添加记录日志功能的相应代码
# def fun1():
#     print("This is fun")
#     # 添加记录日志代码
#     logging.info("fun is running")
#
#
# fun1()


# 如果其他函数具有同样的需求，在每个函数中添加logging,则造成大量的代码冗余
# 为了减少重复代码，可以重新定义一个函数，专门进行日志处理，日志处理完成再执行业务代码
# def use_logging(fun):
#     logging.warning("%s is running" % fun.__name__)
#     fun()


# def fun2():
#     print("this is fun2")
#
#
# use_logging(fun2)
# 这样做，每次都要将一个参数传递给use_logging函数
# 这样新定义日志处理函数，破坏了原有的代码逻辑结构，之前执行业务逻辑时，直接执行gun2()，现在需要执行use_logging(fun2)
# 在不破坏原来代码的业务逻辑，同时完成需求功能就要使用装饰器了

# 【示例2 简单装饰器】**************************************************************************************************
# def use_logging(func):
#     """
#     函数use_logging就是装饰器
#     :param func:
#     :return:
#     """
#     def wrapper(*args, **kwargs):
#         logging.warning("%s is running" % func.__name__)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# def fun():
#     print("This is fun")
#
#
# fun = use_logging(fun)
# fun()
# output:
# WARNING:root:fun is running
# This is fun

"""
函数use_logging就是装饰器，它把执行真正业务方法的func包裹在函数里面，看起来像bar被use_logging装饰了。
在这个例子中，函数进入和退出时 ，被称为一个横切面(Aspect)，这种编程方式被称为面向切面的编程(Aspect-Oriented Programming)。
"""

# @符号是装饰器的语法糖，在定义函数的时候使用，避免再一次赋值操作
# def use_logging(func):
#     """
#     函数use_logging就是装饰器
#     :param func:
#     :return:
#     """
#
#     def wrapper(*args, **kwargs):
#         logging.warning("%s is running" % func.__name__)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @use_logging
# def foo():
#     print("I am foo")
#
#
# @use_logging
# def bar():
#     print("I am bar")


# foo()
# output
# I am foo
# WARNING:root:foo is running

# bar()
# output
# I am foo
# WARNING:root:bar is running

# 【示例3 带参数的装饰器】**************************************************************************************************
"""
装饰器还有更大的灵活性，例如带参数的装饰器：在上面的装饰器调用中，比如@use_logging，该装饰器唯一的参数就是执行业务的函数。
装饰器的语法允许我们在调用时，提供其它参数，比如@decorator(a)。这样，就为装饰器的编写和使用提供了更大的灵活性。
"""


def use_logging(level):
    """
    use_logging是允许带参数的装饰器。
    :param level:
    :return: 实际上是对原有装饰器的一个函数封装，并返回一个装饰器。
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warning("%s is running" % func.__name__)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@use_logging(level="warn")
def foo(name="foo"):
    print("I am %s" % name)


# foo()
# output
# I am foo
# WARNING:root:foo is running

"""
上面的use_logging是允许带参数的装饰器。
它实际上是对原有装饰器的一个函数封装，并返回一个装饰器。
我们可以将它理解为一个含有参数的闭包。
当我们使用@use_logging(level="warn")调用的时候，Python能够发现这一层的封装，并把参数传递到装饰器的环境中。

装饰器在Python使用如此方便都要归因于Python的函数能像普通的对象一样能作为参数传递给其他函数，
可以被赋值给其他变量，可以作为返回值，可以被定义在另外一个函数内。
"""

# 【示例4 类装饰器】**************************************************************************************************
"""
类装饰器，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。
使用类装饰器还可以依靠类内部的__call__方法，当使用@形式将装饰器附加到函数上时，就会调用此方法。
"""


class Foo(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("class decorator running")
        self.func()
        print("class decorator ending")


@Foo
def bar():
    print("this is bar")


# bar()
# output
# class decorator running
# this is bar
# class decorator ending

# 【示例5  functools.wraps】*******************************************************************************************
# 使用装饰器极大地复用了代码，但是他有一个缺点就是原函数的元信息不见了，比如函数的docstring、__name__、参数列表，先看例子：
def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logged
def foo(x):
    """does some math"""
    return x + x * x


print(foo.__name__)  # with_logging
print(foo.__doc__)  # None


# 不难发现，函数foo被with_logging取代了，当然它的docstring，__name__就是变成了with_logging函数的信息了。
# 这个问题就比较严重的，此时需要借助functools.wraps，
# wraps本身也是一个装饰器，它能把原函数的元信息拷贝到装饰器函数中，这使得装饰器函数也有和原函数一样的元信息了。

def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + "was called")
        return func(*args, **kwargs)

    return with_logging


@logged
def bar(x):
    """dose some math"""
    return x ** 2 + x


print(bar.__name__)  # bar
print(bar.__doc__)  # dose some math

# 【示例6  内置装饰器】*******************************************************************************************
# @staticmathod、@classmethod、@property

# 【示例7  内置装饰器】*******************************************************************************************
"""
# 装饰器的顺序
@a
@b
@c
def f():
    pass

# 等效于:
f = a(b(c(f)))
"""
# 注:以上整理于: https://www.zhihu.com/question/26930016 刘志军老师回答


# 【Python进阶 示例】*******************************************************************************************
def a_new_decorator(a_func):
    """
    定义装饰器
    :param a_func: 传递参数 函数
    :return:
    """
    def wrap_the_function():
        print('I am doing some boring work before executing a_func()')
        a_func()
        print('I am doing some boring work after executing a_func()')

    return wrap_the_function

def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print('I am the function which needs some decoration to remove my foul smell')


a_function_requiring_decoration()
# output
# I am the function which needs some decoration to remove my foul smell


a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()
# output
# I am doing some boring work before executing a_func()
# I am the function which needs some decoration to remove my foul smell
# I am doing some boring work after executing a_func()

print(a_function_requiring_decoration.__name__)
# output
# wrap_the_function
"""
这并不是我们想要的！Ouput输出应该是“a_function_requiring_decoration”。 
这⾥的函数被warpTheFunction替代了。 
它重写了我们函数的名字和注释⽂档(docstring)。 
Python提供给我们⼀个简单的函数来解决这个问题， 那就是functools.wraps。
07_decorators_first-2.py 示例代码
"""