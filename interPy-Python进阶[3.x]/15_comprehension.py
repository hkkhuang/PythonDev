#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 15_comprehension.py
# Author        : huangkeke
# Time          : 2018/6/11 8:49
# Contact       : hkkhuang@163.com
# Description	: 推倒式 comprehension

# 推导式又称为解析式，是Python的一种独有特性，可以从一个数据序列构建另一个新的数据序列的结构体。
# 共有三种推导：
# 列表（list）推导式
# 字典（dict）推导式
# 集合（set）推导式

# *************************************************************************************************************
# 列表推导式 list comprehensions
# 列表推导式又称列表解析式，提供一种简明扼要的方法创建列表
# 它的结构是在一个中括号里包含一个表达式，然后是一个for语句，然后是0个或者多个for或者if语句
# 表达式是任意的，意思是可以在列表中放入任意类型的对象，
# 返回结果是一个新的列表，在这个以if和for语句为上下文德尔表达式运行完成之后产生
# 规范
# variable = [out_exp for out_exp in input_list if out_exp == 2]


def list_comprehension():
    multiples = [i for i in range(30) if i % 3 is 0]
    print(multiples)
    # output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]


# 列表推导式在有些情况下使用非常方便， 特别是当你需要使⽤for循环来⽣成⼀个新列表
# 如
def list_new():
    squared = []
    for x in range(10):
        squared.append(x ** 2)
    print(squared)
    # output:
    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# 使用列表推导式可以简化为：
def list_comprehension2():
    squared = [x ** 2 for x in range(10)]
    print(squared)
    # output:
    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# *************************************************************************************************************
# 字典推导式 dict comprehensions
# 字典推导和列表推导的使⽤⽅法是类似的
def dict_comprehension():
    """
    把同⼀个字母但不同⼤⼩写的值合并起来
    :return:
    """
    mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
    mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys()}
    print(mcase_frequency)
    # output:
    # {'a': 17, 'b': 34, 'z': 3}


def dict_comprehension2():
    """
    快速对换⼀个字典的键和值：
    """
    # {v: k for k, v in some_dict.items()}
    information = {'name': 'Tom', 'age': 20, 'gendere': 'M'}
    information = {v: k for k, v in information.items()}
    print(information)
    # {'Tom': 'name', 20: 'age', 'M': 'gendere'}


# **********************************************************************************************************】
# 集合推导式（set comprehensions）
# 跟列表推导式也是类似的。 唯⼀的区别在于它们使⽤⼤括号{}

def set_comprehension():
    squared = {x ** 2 for x in [1, 1, 2]}
    print(squared)
    # Output: {1, 4}


def main():
    list_comprehension()
    list_new()
    list_comprehension2()
    dict_comprehension()
    dict_comprehension2()
    set_comprehension()


if __name__ == '__main__':
    main()
