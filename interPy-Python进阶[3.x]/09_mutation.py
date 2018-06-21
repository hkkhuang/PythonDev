#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 09_mutation.py
# Author        : huangkeke
# Time          : 2018/6/8 12:01
# Contact       : hkkhuang@163.com
# Description	:

foo = ['hi']
print(foo)
# output: ['hi']

bar = foo
bar += ['bye']
print(foo)
# output: ['hi', 'bye']

print(bar)
# output: ['hi', 'bye']

"""
这是对象可变性(mutability)在作怪。 
每当你将⼀个变量赋值为另⼀个可变类型的变量时， 对这个数据的任意改动会同时反映到这两个变量上去。 
新变量只不过是⽼变量的⼀个别名⽽已。 
"""


#  *****************************************************************************************************
def append_to(num, target=[]):
    target.append(num)
    return target


print(append_to(1))
# output: [1]
print(append_to(2))
# output: [1, 2]
print(append_to(3))
# output: [1, 2, 3]

"""
# 一开始可能是希望调⽤append_to时， 有⼀个新的列表被创建
# 希望输出的结果如下：
print(append_to(1))
# output: [1]
print(append_to(2))
# output: [2]
print(append_to(3))
# output: [3]
"""


# 最终的输出结果并不是上面所期望的结果
# 原因是列表的可变性, 在Python中当函数被定义时， 默认参数只会运算⼀次， ⽽不是每次被调⽤时都会重新运算。
# 永远不要定义可变类型的 默认参数， 除⾮你知道你正在做什么。


# ****************************************************************************************************************
# 如果使用可变类型做默认参数  可以按照以下方式做:
def append_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

# 现在再调⽤这个函数不传⼊target参数的时候， ⼀个新的列表会被创建:
print(append_to(1))
# output: [1]
print(append_to(2))
# output: [2]
print(append_to(3))
# output: [3]
