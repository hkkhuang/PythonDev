#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 08_global_return.py
# Author        : huangkeke
# Time          : 2018/6/7 8:29
# Contact       : hkkhuang@163.com
# Description	: global,return用法

# 注意: 尽量避免使用global


# ***************************************************************************************************************
def add1(value1, value2):
    """
    加法运算:函数将两个值作为输入， 然后输出它们相加之和
    :param value1: 加数1
    :param value2: 加数2
    :return: 两个数之和
    """
    return value1 + value2


result1 = add1(1, 2)
print(result1)


# ***************************************************************************************************************
def add2(value1, value2):
    """
    加法运算:函数将两个值作为输入， 然后输出它们相加之和
    :param value1: 加数1
    :param value2: 加数2
    :return:
    """
    global result2  # global变量意味着我们可以在函数以外的区域都能访问这个变量。
    result2 = value1 + value2


add2(3, 5)
print(result2)


# ***************************************************************************************************************
def add3(value1, value2):
    result3 = value1 + value2


add3(2, 3)


# print(result3)  # NameError: name 'result3' is not defined


# 报错,没有定义变脸result3
# 这是因为result3变量只能在创建它的函数内才允许访问,除非它是全局的

# ***************************************************************************************************************
# 多个return值
# 想从⼀个函数⾥返回两个变量⽽不是⼀个呢？
# 新⼿们多使用的方法是使⽤global关键字。下面这个没⽤的例⼦：
def profile1():
    global name1
    global age1
    name1 = "Tom"
    age1 = 20


profile1()
print(name1)
print(age1)


# 注意: 不要试着使⽤上述⽅法。 重要的事情说三遍， 不要试着使⽤上述⽅法！


# ***************************************************************************************************************
# 另一个方法是函数结束时， 返回⼀个包含多个值的tuple(元组)， list(列表)或者dict(字典),来解决这个问题,这是⼀种可⾏的⽅式。
def profile2():
    name2 = "Mark"
    age2 = 18
    return (name2, age2)


profile_data = profile2()
print(profile_data[0])  # Mark
print(profile_data[1])  # 18


# ***************************************************************************************************************
# 按照更常见的惯例：
def profile3():
    name3 = "Jerry"
    age3 = 16
    return name3, age3
# 这是⼀种⽐列表和字典更好的⽅式。


profile_data2 = profile3()
print(type(profile_data2))  # <class 'tuple'>
print(profile_data2[0])  # Jerry
print(profile_data2[1])  # 16
