# -*- coding: utf-8 -*-
# @Time : 2019/8/21 13:29
# @Author : wangmengmeng
# from log.record_log import log
# log.info('模块被导入打印日志')

from collections import namedtuple
MyTupleClass = namedtuple('MyTupleClass',['name', 'age', 'job'])
obj = MyTupleClass("Tomsom",12,'Cooker')
print(obj.name)
print(obj.age)
print(obj.job)