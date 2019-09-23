# -*- coding: utf-8 -*-
# @Time : 2019/9/23 16:58
# @Author : wangmengmeng
import threading

def test():
    """单线程执行"""
    print("this is a testing code.")
t = threading.Thread(target=test)
t.start()