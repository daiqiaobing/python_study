# -*- coding: utf-8 -*-
# 继承式调用方式
import random
import threading

import time


class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        time.sleep(random.randint(0, 3))
        print 'the number is %s!' % self.num


if __name__ == '__main__':
    for index in range(100):
        MyThread(index).start()
