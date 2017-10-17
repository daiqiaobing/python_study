# -*- coding: utf-8 -*-
# 通过Event来实现两个或多个线程间的交互 下面是一个红绿灯的例子
import random
import threading

import time


def light():
    if not event.isSet():
        event.set()
    count = 0
    while True:
        if count < 10:
            print '\033[42;1m--green light on---\033[0m'
        elif count < 13:
            print '\033[43;1m--yellow light on---\033[0m'
        elif count < 20:
            if event.isSet():
                event.clear()  # 继续阻塞
            print '\033[41;1m--red light on---\033[0m'
        else:
            count = 0
            event.set()  # 唤醒所有的event， 处于等待状态
        time.sleep(1)
        count += 1


def car(n):
    while True:
        time.sleep(random.randrange(10))
        if event.isSet():  # 绿灯
            print "car [%s] is running.." % n
        else:
            print "car [%s] is waiting for the red light.." % n


if __name__ == '__main__':
    event = threading.Event()
    light = threading.Thread(target=light)
    light.start()
    for i in range(4):
        threading.Thread(target=car, args=(i,)).start()