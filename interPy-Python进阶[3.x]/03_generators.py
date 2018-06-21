#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 03_generators.py
# Author        : huangkeke
# Time          : 2018/6/2 11:39
# Contact       : hkkhuang@163.com
# Description	: 迭代器和生成器

# 示例 01
def generator_function():
    """
    生成器函数
    :return:
    """
    for i in range(10):
        yield i


def print_generator_function():
    for item in generator_function():
        print(item)


def fibon(n):
    """
    斐波那契数列生成器
    :param n: 生成数列长度
    :return:
    """
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fibonacci():
    """
    调用fibon(n) 斐波那契数列生成函数
    :return:
    """
    for x in fibon(100000):  # 传入生成长度
        print(x)


# 示例 01
# def main():
#     print_generator_function()


def fibon(n):
    """
    使用列表实现斐波那契数列
    :param n: 生成数列个数
    :return: 返回存储生成数列的列表
    这样会消耗大量资源，尤其是在生成一个很大的数列长度时
    """
    a = b = 1
    result = []
    for i in range(n):
        result.append(i)
        a, b = b, a + b
    return result


def generator_function_next():
    """
    ⽣成器使⽤⼀次迭代， 输出需要用到ython内置函数： next()。
     它允许我们获取⼀个序列的下⼀个元素。
    :return:
    """
    for i in range(5):
        yield i


def print_generator_function_next():
    generator = generator_function_next()
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))

    print(next(generator))  # 异常报错
    # Traceback(most recent call last):
    # StopIteration


def iter_function():
    """
    Python内置函数 iter()
    根据一个可迭代对象返回一个迭代器
    :return:
    """
    my_string = "huangkeke"
    # print(next(my_string))  # 直接迭代输出 报错  str对象是一个可迭代对象，但不是一个迭代器
    # 需要使用内置函数iter 根据一个可迭代对象返回一个迭代器对象
    my_iter = iter(my_string)
    for item in my_iter:
        print(item)


def main():
    # 示例 01
    # fibonacci()

    # 示例 02
    # print_generator_function_next()

    iter_function()


if __name__ == '__main__':
    main()

"""
迭代器
迭代器是一个可以遍历伊戈尔容器（特别是列表）的对象。
注意：一个迭代器在遍历并读取一个容器的数据时并不会执行一个迭代。

理解下面三个概念：
1.可迭代对象（Iterable）
2.迭代器（Iterator）
3.迭代（Iteration）

可迭代对象(Iterable)
⼀个可迭代对象是Python中任意的对象， 只要它定义了可以返回⼀个迭代器的__iter__⽅法， 
或者定义了可以⽀持下标索引的__getitem__⽅法。 
⼀个可迭代对象就是任意的对象， 只要这个对象能给我们提供⼀个迭代器。

迭代器(Iterator)
⼀个迭代器是任意⼀个对象， 只要它定义了⼀个next(Python2) 或者__next__⽅法。

迭代(Iteration)
迭代简单讲就是从某个容器（⽐如⼀个列表） 取出⼀个元素的过程。 
当使⽤⼀个循环来遍历某个东西时， 这就叫⼀个迭代。 

⽣成器(Generators)
⽣成器也是⼀种迭代器， 但是只能对其迭代⼀次。 
因为生成器并没有把所有的值存在内存中， ⽽是在运⾏时⽣成值。 
通过遍历来使⽤它们， 要么⽤⼀个“for”循环， 要么将它们传递给任意可以进⾏迭代的函数和结构。 
通常⽣成器是以函数来实现的。注意：函数并不返回⼀个值， ⽽是yield(“⽣出”)⼀个值。 

⽣成器最佳应⽤场景是： 你不想同⼀时间将所有计算出来的⼤量结果集分配到内存当中， 特别是结果集⾥还包含循环。
注： 这样会消耗⼤量资源

⽣成器使⽤⼀次迭代，输出需要用到⼀个Python内置函数： next()。 它允许我们获取⼀个序列的下⼀个元素。 
在yield掉所有的值后， next()触发了⼀个StopIteration的异常。基本上这个异常告诉我们， 所有的值都已经被yield完了。 

使⽤for循环时没有写next函数，其实是for循环自动调用了next()方法。
同时使⽤for循环时没有 StopIteration 这个异常，因为 for循环会⾃动捕捉到这个异常并停⽌调⽤next()。 

Python中⼀些内置数据类型也⽀持迭代：如str对象；
直接迭代出现异常，异常说str对象不是⼀个迭代器。 
str对象是⼀个可迭代对象， ⽽不是⼀个迭代器。 这意味着它⽀持迭代， 但我们不能直接对其进⾏迭代操作。 
想要对它实施迭代需要⼀个内置函数--iter。 这个函数将根据⼀个可迭代对象返回⼀个迭代器对象。 
"""
