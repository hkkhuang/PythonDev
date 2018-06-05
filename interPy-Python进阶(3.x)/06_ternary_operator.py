#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 06_ternary_operator.py
# Author        : huangkeke
# Time          : 2018/6/5 8:49
# Contact       : hkkhuang@163.com
# Description	: 三元运算符


def ternary_operator_one():
    """
    三元运算符-条件表达式（1）
    :return:
    """
    is_fat = True
    state = "fat" if is_fat else "not fat"
    print(state)

    a, b = 1, 2
    result = a > b
    print("a > b") if result else print("a <= b")


def ternary_operator_two():
    fat = True
    fitness = ("skinny", "fat")[fat]
    print(fitness)


def main():
    ternary_operator_one()
    ternary_operator_two()


if __name__ == '__main__':
    main()
"""
三元运算符 又称为条件表达式，这些表达式基于真（true）/假(false)判断

#【1】如果条件为真， 返回真 否则返回假
condition_is_true if condition else condition_is_false
条件为真结果 if 条件 else 条件为假结果

is_fat = True
state = "fat" if is_fat else "not fat"

# 【2】另⼀个晦涩⼀点的⽤法⽐较少见， 使⽤了元组：
伪代码:
#(返回假， 返回真)[真或假]
(if_test_is_false, if_test_is_true)[test]
# 在Python中， True等于1， ⽽False等于0， 这就相当于在元组中使⽤0和1来选取数据。

例⼦:
fat = True
fitness = ("skinny", "fat")[fat]
print("Ali is ", fitness)
#输出: Ali is fat

上⾯的例⼦没有被⼴泛使⽤， ⽽且Python玩家⼀般不喜欢那样， 因为没有Python味⼉(Pythonic)。 
这样的⽤法很容易把真正的数据与true/false弄混。

另外⼀个不使⽤元组条件表达式的缘故是因为在元组中会把两个条件都执⾏， ⽽ if-else 的条件表达式不会这样。
condition = True
print(2 if condition else 1/0)
#输出: 2

print((1/0, 2)[condition])
#输出ZeroDivisionError异常

在元组中是先建数据， 然后⽤True(1)/False(0)来索引到数据。
 ⽽if-else条件表达式遵循普通的if-else逻辑树， 因此， 如果逻辑中的条件异常， 或者是重计算型（计算较久） 的情况下， 最好尽量避免使⽤元组条件表达式。
"""
