#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 04_map_filter.py
# Author        : huangkeke
# Time          : 2018/6/3 10:12
# Contact       : hkkhuang@163.com
# Description	: map和filter用法

# 书中代码 map,filter 前面的list是多余的，因为map本来就会返回一个list
# 注：需要将结果转为list类型输出

# Start**************************************************************************************************************
# 把列表中所有元素⼀个个地传递给⼀个函数， 并收集输出。
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i ** 2)

# Map⽤⼀种简单⽽漂亮得多的⽅式来实现
items = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, items)
print(squared)  # <map object at 0x000001B91099B710>
print(type(squared))  # <class 'map'>

# ⼤多数时候， 使⽤匿名函数(lambdas)来配合map
# 需要转换为list
squared = list(map(lambda x: x ** 2, items))
print(squared)


# [1, 4, 9, 16, 25]
# End****************************************************************************************************************


# Start**************************************************************************************************************
# 不仅⽤于⼀列表的输⼊， 我们甚⾄可以⽤于⼀列表的函数
def multiply(x):
    """
    乘法函数
    :param x: 需要做乘法的数据
    :return:  完成乘法运算后结果
    """
    return x * x


def add(x):
    """
    加法运算函数
    :param x: 需要做加法的数据
    :return:  完成加法运算后的结果
    """
    return x + x


# 列表的函数
funcs = [multiply, add]
# print(type(funcs[1]))  # <class 'function'> 列表中元素类型是function
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
print(value)


# [16, 8]  1*2*3*4  1+2+3+4
# End****************************************************************************************************************

# Start**************************************************************************************************************
# filter能创建⼀个列表， 其中每个元素都是对⼀个函数能返回True.
def less_zero(x):
    """
    判断一个元素是否条件
    :param x: 需要判断元素
    :return: 返回判断结果
    """
    return x < 0


number_list = range(-5, 5)
# print(type(number_list))  # <class 'range'>
# less_than_zero = list(filter(lambda x: x < 0, number_list))  # 与下面同样功能
less_than_zero = list(filter(lambda x: less_zero(x), number_list))  # 为了更好的演示【每个元素都是对⼀个函数能返回True.】
print(less_than_zero)


# Output: [-5, -4, -3, -2, -1]
# End****************************************************************************************************************

# Start**************************************************************************************************************
# filter()函数用于过滤序列。
def is_odd(n):
    """
    过滤偶数数据，保留奇数数据
    :param n: 需要过滤的数据
    :return: 返回过滤后德尔数据，保留的奇数
    """
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
# Output: [1, 5, 9, 15]
# End****************************************************************************************************************

""""
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

Map会将⼀个函数映射到⼀个输⼊列表的所有元素上。 
规范：map(function_to_apply, list_of_inputs)
⼤多数时候， 使⽤匿名函数(lambdas)来配合map

**补充【匿名函数】
当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
也可以把匿名函数作为返回值返回

Filter
顾名思义， filter能创建⼀个列表， 其中每个元素都是对⼀个函数能返回True.
filter类似于⼀个for循环， 是⼀个内置函数， 并且更快。

filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
"""