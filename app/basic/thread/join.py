# -*- coding: utf-8 -*-
import threading
import time


def run(n):
    print '[%s]---------running--------\n' % n
    time.sleep(2)
    print '----done-----'


def main():
    for index in range(5):
        t = threading.Thread(target=run, args=(index,))
        t.start()
        t.join(2)
        print 'starting  thread, the name is %s' % t.getName()


if __name__ == '__main__':
    m = threading.Thread(target=main, args=[])
    m.setDaemon(True)  # 设置为守护线程,它作为程序的主线程，当主线程退出时,m线程也会退出,
    # 由m启动的其它子线程会同时退出,不管是否执行完任务
    m.start()
    m.join(timeout=3)
    print("---main thread done----")
