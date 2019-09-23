# -*- coding: utf-8 -*-
# @Time : 2019/9/23 17:31
# @Author : wangmengmeng
import threading
from datetime import *


def test():
    x = 0
    while(x == 0):
        print(datetime.now())


def thd():
    Threads = []
    for i in range(10):
        t = threading.Thread(target=test)
        Threads.append(t)
        t.setDaemon(True)
    for t in Threads:
        t.start()



if __name__ == '__main__':
    thd()
    print('end')
