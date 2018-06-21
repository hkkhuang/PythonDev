#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 12_collection.py
# Author        : huangkeke
# Time          : 2018/6/9 20:24
# Contact       : hkkhuang@163.com
# Description	: 容器-collections.
"""
Python附带⼀个模块， 它包含许多容器数据类型， 名字叫作collections.
主要介绍：
defaultdict
counter
deque
namedtuple
enum.Enum (包含在Python 3.4以上)
"""
# ******************************************************************************************************************
# defaultdict
# 与dict类型不同， 不需要检查key是否存在
from collections import defaultdict

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)
# defaultdict(<class 'list'>, {'Yasoob': ['Yellow', 'Red'], 'Ali': ['Blue', 'Black'], 'Arham': ['Green'], 'Ahmed': ['Silver']})


# ****************************************************************************************************************
# 另⼀种重要的是例⼦： 在⼀个字典中对⼀个键进⾏嵌套赋值时， 如果这个键不存在， 会触发keyError异常。
# defaultdict允许⽤⼀个聪明的⽅式绕过这个问题。⾸先是⼀个使⽤dict触发KeyError的例⼦， 然后提供⼀个使⽤defaultdict的解决⽅案
# some_dict = {}
# some_dict['colours']['favourite'] = 'yellow'
# print(some_dict)
# KeyError: 'colours'

# 解决方案:
import collections

tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = 'yellow'
print(some_dict)
# defaultdict(<function <lambda> at 0x000001DEC6592EA0>, {'colours': defaultdict(<function <lambda> at 0x000001DEC6592EA0>, {'favourite': 'yellow'})})

# 以⽤json.dumps打印出some_dict， 例如：
import json

print(json.dumps(some_dict))
# {"colours": {"favourite": "yellow"}}

# ****************************************************************************************************************
# counter
# Counter是⼀个计数器， 它可以帮助我们针对某项数据进⾏计数。 ⽐如它可以⽤来计算每个⼈喜欢多少种颜⾊：
from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)
favs = Counter(name for name, colour in colours)
print(favs)
# Counter({'Yasoob': 2, 'Ali': 2, 'Arham': 1, 'Ahmed': 1})

# 也可以在利⽤它统计⼀个⽂件， 例如：
with open('explore.txt', 'rb') as f:
    line_count = Counter(f)
print(line_count)

# ****************************************************************************************************************
# deque提供了⼀个双端队列， 你可以从头/尾两端添加或删除元素。 要想使⽤它， ⾸先我们要从collections中导⼊deque模块：
from collections import deque

d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))
# output: 3

print(d[0])
# output: 1

print(d[-1])
# output: 3

d = deque(range(5))
print(len(d))
# output: 5

# 可以从两端取出(pop)数据：
print(d.popleft())
# output: 0

print(d.pop())
# output: 4
# pop 默认从右边弹出

# 也可以限制这个列表的⼤⼩， 当超出你设定的限制时， 数据会从对队列另⼀端被挤出去(pop)。
d = deque(maxlen=30)
for i in range(35):
    d.append(i)
# 默认是右边添加，左边挤出去
print(d)
# deque([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], maxlen=30)

# 还可以从任意一端进行扩展：
d = deque([1, 2, 3, 4, 5])
d.extendleft([0])
d.extend([6, 7, 8, 9])
print(d)
# deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# **********************************************************************************************************
# namedtuple
# 一个元组是⼀个不可变的列表， 可以存储⼀个数据的序列， 和命名元组(namedtuples)⾮常像， 但有⼏个关键的不同。
# 主要相似点是都不像列表， 不能修改元组中的数据。
# 为了获取元组中的数据， 需要使⽤整数作为索引：

man = ('Ali', 30)
print(man[0])
# Ali

# namedtuples是什么呢？
# 它把元组变成⼀个针对简单任务的容器。 你不必使⽤整数索引来访问⼀个namedtuples的数据。
# 可以像字典(dict)⼀样访问namedtuples,但namedtuples是不可变的。
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name='perry', age=31, type='cat')
print(perry)
# Animal(name='perry', age=31, type='cat')

print(perry.name)
# perry
# 可以⽤名字来访问namedtuple中的数据。 我们再继续分析它。
# ⼀个命名元组(namedtuple)有两个必需的参数。 它们是元组名称和字段名称。

# 在上⾯的例⼦中， 我们的元组名称是Animal， 字段名称是'name'， 'age'和'type'。
# namedtuple让你的元组变得⾃⽂档了。 你只要看⼀眼就很容易理解代码是做什么的。
# 你也不必使⽤整数索引来访问⼀个命名元组， 这让你的代码更易于维护。
# ⽽且， namedtuple的每个实例没有对象字典， 所以它们很轻量， 与普通的元组⽐， 并不需要更多的内存。 这使得它们⽐字典更快。
# 要记住它是⼀个元组， 属性值在namedtuple中是不可变的

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
# perry.age = 42
# AttributeError: can't set attribute


from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry[0])
# 输出: perry

# 最后， 你可以将⼀个命名元组转换为字典， ⽅法如下：
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type="cat")
print(perry._asdict())
# OrderedDict([('name', 'Perry'), ('age', 31), ('type', 'cat')])

# *****************************************************************************************************************
# 另⼀个有⽤的容器是枚举对象， 它属于enum模块， 存在于Python 3.4以上版本中
# 让我们回顾⼀下上⼀个'Animal'命名元组的例⼦。
# 它有⼀个type字段， 问题是， type是⼀个字符串。
# 那么问题来了， 万⼀程序员输⼊了Cat， 因为他按到了Shift键， 或者输⼊了'CAT'， 甚⾄'kitten'？
from collections import namedtuple
from enum import Enum


class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # 依次类推
    # 但我们并不想关⼼猫咪的年纪(译者注： 作者的意思是cat, kitten, puppy， 都是猫咪， 只
    kitten = 1
    puppy = 2


Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)

print(charlie.type == tom.type)
# output：True
print(charlie.type)
# Species.cat

# 有三种⽅法访问枚举数据， 例如以下⽅法都可以获取到'cat'的值：
print(Species(1))
print(Species['cat'])
print(Species.cat)

