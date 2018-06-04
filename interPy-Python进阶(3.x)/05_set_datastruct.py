#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 05_set_datastruct.py
# Author        : huangkeke
# Time          : 2018/6/4 8:08
# Contact       : hkkhuang@163.com
# Description	: Set Types — set, frozenset


def check_list_elements():
    """
    使用普通方法，遍历列表，一次判断列表元素是否重复
    :return:
    """
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']  # 待检查列表
    repeats = []  # 结果存放列表
    for value in some_list:  # 依次遍历some_list中的元素
        if some_list.count(value) > 1:  # 判断该元素在some_list的个数，count>1 说明重复
            if value not in repeats:  # 再判断value是否已经在duplicates中（some_list中某个元素多次重复），duplicates只记录一次
                repeats.append(value)  # 将some_list中重复的元素并且尚未添加到duplicates中的，添加进duplicates
    print(repeats)  # 输出结果


def duplicates(some_list):
    """
    使用set检查列表中是否包含重复的元素
    :param some_list:
    :return:
    """
    return set([x for x in some_list if some_list.count(x) > 1])


def intersect():
    """
    两个集合的交集
    :return:
    """
    valid = set(['yellow', 'red', 'blue', 'green', 'black'])
    input_set = set(['red', 'brown'])
    print(input_set.intersection(valid))  # 交集运算
    print(valid & input_set)   # 交集运算


def union():
    """
    两个集合的并集
    :return:
    """
    valid = set(['yellow', 'red', 'blue', 'green', 'black'])
    input_set = set(['red', 'brown'])
    print(input_set.union(valid))  # 并集运算
    print(valid | input_set)   # 并集运算



def difference():
    """"
    两个集合的差集
    """
    valid = set(['yellow', 'red', 'blue', 'green', 'black'])
    input_set = set(['red', 'brown'])
    print(input_set.difference(valid))  # 差集运算
    print(input_set - valid)  # 差集运算


def main():
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    check_list_elements()
    print(duplicates(some_list))
    intersect()   # 集合交集
    union()       # 集合并集
    difference()  # 集合差集


if __name__ == '__main__':
    main()

"""
set(集合)数据结构
set(集合)与列表(list)的⾏为类似， 区别在于set不能包含重复的值。
set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等

set 语法：class set([iterable])
参数说明：iterable -- 可迭代对象对象；
  返回值: 返回新的集合对象。
  
 可以使用花括号或set()函数创建集合。注意:要创建空集，必须使用set()而不是{};后者创建一个空的字典
 
集合对象是一组不同的hashable对象的无序集合。
常见的用途：成员关系测试、从序列中删除重复项，以及计算数学运算，如相交、合并、差异和对称差异。
(对于其他容器，请参见内置的dict、list和tuple类以及collections模块。)

与其他集合一样，set x in set, len(set), and for x in set. 
set是无序集合，不记录元素位置或插入顺序。因此，set不支持索引、切片或其他类似序列的行为。

目前有两个内置的set类型，set和frozenset。
set类型是可变的——可以使用add()和remove()等方法更改内容。
由于它是可变的，所以没有哈希值，不能用作字典键或其他集合的元素。
frozenset类型是不可变的、hashtable——它的内容在创建后不能更改;因此，它可以用作字典键或其他集合的元素。
除了set构造函数之外，还可以在大括号内放置一个以逗号分隔的元素列表，例如:{'jack'、'sjoerd'}，创建非空集(不是frozensets)。

Instances of set and frozenset provide the following operations:
len(s)  
# Return the number of elements in set s (cardinality of s).

x in s
# Test x for membership in s.

x not in s
# Test x for non-membership in s.

isdisjoint(other)
# Return True if the set has no elements in common with other. Sets are disjoint if and only if their intersection is the empty set.

issubset(other)
set <= other
# Test whether every element in the set is in other.

set < other
Test whether the set is a proper subset of other, that is, set <= other and set != other.

issuperset(other)
set >= other
# Test whether every element in other is in the set.

set > other
# Test whether the set is a proper superset of other, that is, set >= other and set != other.

union(*others)
set | other | ...
# Return a new set with elements from the set and all others.

intersection(*others)
set & other & ...
# Return a new set with elements common to the set and all others.

difference(*others)
set - other - ...
# Return a new set with elements in the set that are not in the others.

symmetric_difference(other)
set ^ other
# Return a new set with elements in either the set or other but not both.

copy()
# Return a new set with a shallow copy of s.
"""
