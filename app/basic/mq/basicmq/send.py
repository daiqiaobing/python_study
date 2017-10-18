# _*_coding:utf-8_*_
import random

import pika

__author__ = 'mango'

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')
    body = 'mango %s' % random.randint(0, 1000)
    channel.basic_publish(exchange='', routing_key='hello', body=body)
    print " [x] Sent '%s'" % body
    connection.close()
