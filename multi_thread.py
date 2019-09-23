# -*- coding: utf-8 -*-
# @Time : 2019/9/23 17:02
# @Author : wangmengmeng
import threading
from datetime import *


def test():
    print(datetime.now())
    # print("this is a testing code.")


def thd():
    Threads = []
    for i in range(10):
        t = threading.Thread(target=test)
        Threads.append(t)
    for t in Threads:
        t.start()


if __name__ == '__main__':
    thd()
