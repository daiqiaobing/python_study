# _*_coding:utf-8_*_
import random

import datetime
import pika
import sys

import time

__author__ = 'mango'

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue')
    while True:
        time.sleep(1)
        message = 'hello world %s' % datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S %p')
        channel.basic_publish(exchange='', routing_key='task_queue', body=message,
                              properties=pika.BasicProperties(delivery_mode=2))
        print " [x] Sent '%s'" % message
    connection.close()
