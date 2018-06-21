#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 1_args_kwargs.py
# Author        : huangkeke
# Time          : 2018/4/16 10:02
# Contact       : hkkhuang@163.com
# Description	: *args 和 **kwargs 的用法


def test_var_args(f_arg, *args):
    """
    *args 用来发送一个非键值对的可变数量的参数列表给一个函数
    :param f_arg:  确定传递参数
    :param argv: 传递参数不确定
    :return: 无
    """
    print('first normal arg:', f_arg)
    for arg in args:
        print('another arg though *argv:', arg
        # 输出：
        # first normal arg: hkkhuang
        # another arg though *argv: Tom
        # another arg though *argv: Jerry
        # another arg though *argv: Mark


def test_var_kwargs(**kwargs):
    """
    **kwargs 用来发送不定长度的键值对作为参数传递给一个函数
    :param kwargs: 传递参数数量不确定 且参数为键值对
    :return:
    """
    for key, value in kwargs.items():
        print('{0} == {1}'.format(key, value))
        # 输出
        # name == hkkhuang


def test_args(name, age, score):
    """
    测试用*args和**kwargs调用函数
    :param name:
    :param age:
    :param score:
    :return:
    """
    print("name:", name)
    print("age:", age)
    print("score:", score)


def main():
    """
    调用测试函数
    :return:
    """
    test_var_args('hkkhuang', 'Tom', 'Jerry', 'Mark')
    test_var_kwargs(name='hkkhuang')

    # 测试用 * args和 ** kwargs调用函数
    args = ("Tom", 22, 100)
    test_args(*args)
    # 输出
    # name: Tom
    # age: 22
    # score: 100

    kwargs = {"score": "99", "age": 22, "name": "hkkhuang"}
    test_args(**kwargs)
    # 输出
    # name: hkkhuang
    # age: 22
    # score: 99


if __name__ == '__main__':
    main()

"""
不是必须写成*args 和**kwargs。 只有变量前⾯的 *(星号)才是必须的.                        
也可以写成*var 和**vars.                                                              \
*args 和 **kwargs 主要用于函数定义 可以将不定数量的参数传递给一个函数。                  
注释: 不定的意思是，事先不清楚函数的额使用者会传递多少参数给函数。                       
                                                                                      
*args 用来发送一个非键值对的可变数量的参数列表给一个函数                                
**kwargs 用来发送不定长度的键值对作为参数传递给一个函数  

标准参数与*args 和 **kwargs 的使用顺序：
fun(args, *args, **kwargs)

什么时候使用 *args 和 **kwargs
最常用的是在写 函数装饰器的时候使用

也可以用来做“猴子补丁（monkey patching）”
即 程序运行时候修改某些代码                              
"""
