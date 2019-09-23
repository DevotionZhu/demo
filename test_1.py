# -*- coding: utf-8 -*-
# @Time : 2019/9/23 21:34
# @Author : wangmengmeng
import threading
import time

def thread():
    time.sleep(2)
    print('---子线程结束---')

def main():
    t1 = threading.Thread(target=thread)
    t1.start()
    print('---主线程---结束')

if __name__ == '__main__':
    main()