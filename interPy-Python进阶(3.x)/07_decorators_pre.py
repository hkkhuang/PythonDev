#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 07_decorators_pre.py
# Author        : huangkeke
# Time          : 2018/6/5 9:55
# Contact       : hkkhuang@163.com
# Description	: 装饰器

print("【1 一切皆为对象】******************************************************-")
# 【1 一切皆为对象】
# ⾸先理解下Python中的函数
def hi(name='hkkhuang'):
    return 'hi,' + name


print(hi())
# Output: hi,hkkhuang

# 可以将⼀个函数赋值给⼀个变量， ⽐如
my_hi = hi
# 这⾥没有在使⽤⼩括号， 因为我们并不是在调⽤hi函数,⽽是在将它放在greet变量⾥
print(my_hi())
# Output: hi,hkkhuang

# 如果删掉旧的hi函数， 看看会发⽣什么！
del hi
# print(hi())
# outputs: NameError: name 'hi' is not defined
print(my_hi())
# Output: hi,hkkhuang


print("【2 在函数中定义函数】******************************************************-")
# 【2 在函数中定义函数】
def hi(name='hkkhuang'):
    print('now you are inside the hi() function')

    def greet():
        return 'now you are in the greet() function'

    def welcome():
        return 'now you are in the welcome() function'

    print(greet())
    print(welcome())
    print('now you are back in the hi() function')


hi()
# Output:
# now you are inside the hi() function
# now you are in the greet() function
# now you are in the welcome() function
# now you are back in the hi() function

# ⽆论何时你调⽤hi(), greet()和welcome()将会同时被调⽤。
# 然后greet()和welcome()函数在hi()函数之外是不能访问的：
# greet()
# Outputs: NameError: name 'greet' is not defined

print("【3-从函数中返回函数】******************************************************-")
# 【3-从函数中返回函数】
# 不需要在⼀个函数⾥去执⾏另⼀个函数， 我们也可以将其作为输出返回出来
def hi2(name='hkkhuang'):
    def greet():
        return 'now you are in the greet() function'

    def welcome():
        return 'now you are in the welcome() function'

    if name == 'hkkhuang':
        return greet
    else:
        return welcome
        # 注意：
        # 在if/else语句中我们返回greet和welcome， ⽽不是greet()和welcome()。
        # 为什么那样？ 这是因为当你把⼀对⼩括号放在后⾯， 这个函数就会执⾏；
        # 然⽽如果你不放括号在它后⾯， 那它可以被到处传递， 并且可以赋值给别的变量⽽不去执⾏它。


a = hi2()
print(a)  # a现在指向到hi2()函数中的greet()函数
# <function hi2.<locals>.greet at 0x0000021C10623950>

# 当我们写下a = hi2()， hi2()会被执⾏， ⽽由于name参数默认是yasoob， 所以函数greet被返回了。
# 如果我们把语句改为a = hi(name = "ali")， 那么welcome函数将被返回。
# 我们还可以打印出hi()()， 这会输出now you are in the greet() function。
a = hi2(name='hkk')
print(a)
# <function hi2.<locals>.welcome at 0x0000022B0B8A3F28>

print(a())  # now you are in the welcome() function

print(hi2()())  # now you are in the greet() function
print(hi2(name='hkk')())  # now you are in the welcome() function

print("【4-将函数作为参数传给另⼀个函数】******************************************************-")
# 【4-将函数作为参数传给另⼀个函数】
def hi3():
    return 'hi,hkkhuang!'


def doSomethingBeforeHi(func):
    """
    将函数作为参数传给另⼀个函数
    :param func: 参数是一个函数
    :return:
    """
    print('I am doing some boring work before executing hi3()')
    print(func())


doSomethingBeforeHi(hi3)
# I am doing some boring work before executing hi3()
# hi,hkkhuang!
