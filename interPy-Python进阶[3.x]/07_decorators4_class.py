#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 07_decorators4_class.py
# Author        : huangkeke
# Time          : 2018/6/6 13:15
# Contact       : hkkhuang@163.com
# Description	: 装饰器类

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        log_string = func.__name__ + ' was called'
        print(log_string)

        # 打开logfile文件并写入
        with open(self.logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')
        self.notify()

    def notify(self):
        # logit 至记录日志,不做其他工作
        pass


@logit
def myfun1():
    pass


class email_logit(logit):
    """
    一个logit的实现版本,可以在函数调用的时候发送邮件给管理员
    """

    def __init__(self, email='hkkhuang@163.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        """发送邮件给管理员"""
        pass
