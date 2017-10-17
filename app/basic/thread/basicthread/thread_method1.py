# -*- coding: utf-8 -*-
# 直接调用方式
import random
import threading
import time


def say_hi(num):
    time.sleep(random.randint(0, 5))
    print 'running on number: %s' % num
    time.sleep(3)

if __name__ == '__main__':
    # 生成线程实例 并且启动线程
    for index in range(100):
        threading.Thread(target=say_hi, args=(index,)).start()
