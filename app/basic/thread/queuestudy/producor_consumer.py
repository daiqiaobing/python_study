# -*- coding: utf-8 -*-
# 生产者消费者模式
import random
import threading
from Queue import Queue

import time


def product(name):
    while True:
        count = random.randint(0, 100)
        time.sleep(1)
        if count % 3 == 0:
            q.put(count)
            print '=========用户%s生产了数据: %s' % (name, count)


def consumer(name):
    while True:
        if q.empty():
            time.sleep(1)
            print '用户%s正在等待数据' % name
        else:
            print '--------用户%s消费了数据为%s' % (name, q.get())


if __name__ == '__main__':
    q = Queue()
    threading.Thread(target=product, args=('张三',)).start()
    threading.Thread(target=consumer, args=('李四',)).start()
