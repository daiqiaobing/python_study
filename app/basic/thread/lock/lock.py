# -*- coding: utf-8 -*-
# 互斥锁
import threading
import time


def add_num():
    global num
    print '--get num:%s' % num
    time.sleep(1)
    lock.acquire()
    num -= 1
    lock.release()

if __name__ == '__main__':
    num = 101
    lock = threading.Lock()
    thread_list = []
    for i in range(100):
        t = threading.Thread(target=add_num)
        t.start()
        thread_list.append(t)
    for tl in thread_list:  # 等待所有线程执行完毕
        t.join()
    print 'final num: %s' % num


