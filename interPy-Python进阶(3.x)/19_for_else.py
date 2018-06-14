#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 19_for_else.py
# Author        : huangkeke
# Time          : 2018/6/14 23:17
# Contact       : hkkhuang@163.com
# Description	: for-else语句

# ****************************************************************************************************************
fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print(fruit.capitalize())
# output:
# Apple
# Banana
# Mango

# ****************************************************************************************************************
# for循环还有⼀个else从句， 我们⼤多数⼈并不熟悉。 这个else从句会在循环正常结束时执⾏。 这意味着， 循环没有遇到任何break.

# 有个常见的构造是跑⼀个循环， 并查找⼀个元素。 如果这个元素被找到了， 我们使⽤break来中断这个循环。 有两个场景会让循环停下来。
# 第⼀个是当⼀个元素被找到， break被触发。
# 第⼆个场景是循环结束。

# 现在我们也许想知道其中哪⼀个， 才是导致循环完成的原因。
# ⼀个⽅法是先设置⼀个标记， 然后在循环结束时打上标记。
# 另⼀个是使⽤else从句。

# for/else循环的基本结构：
# for item in container:
#     if search_something(item):
#         # Found it!
#         process(item)
#         break
# else:
#     # Didn't find anything..
#     not_found_in_container()

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
# 会找出2到10之间的数字的因⼦。

# ******************************************************************************************************************
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
    else:
        print(n, ' is a prime number')
