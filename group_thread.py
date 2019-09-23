# -*- coding: utf-8 -*-
# @Time : 2019/9/23 17:25
# @Author : wangmengmeng
import threading
from datetime import *


def test():
    print(datetime.now())


def looptest():
    for i in range(20):
        test()


def thd():
    Threads = []
    for i in range(25):
        t = threading.Thread(target=looptest)
        Threads.append(t)
    for t in Threads:
        t.start()


if __name__ == '__main__':
    thd()
