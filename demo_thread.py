# -*- coding: utf-8 -*-
# @Time : 2019/9/23 22:40
# @Author : wangmengmeng
import threading

THREAD_NUM = 10
ONE_WORKER_NUM = 10
# 总并发数是这两个变量的乘积
def test():
    """测试代码"""

def working():
    global  ONE_WORKER_NUM
    for i in ONE_WORKER_NUM:
        test()

def t():
    global THREAD_NUM
    Threads = []
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working,name="T"+str(i))
        t.setDaemon(True)
        Threads.append(t)
    for t in Threads:
        t.start()
    for t in Threads:
        t.join()


if __name__ == '__main__':
    t()
