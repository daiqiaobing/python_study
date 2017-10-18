# _*_coding:utf-8_*_
import time

__author__ = 'mango'
import pika


def callback(channel, method, properties, body):
    print '[X] Recieved %r ' % body
    time.sleep(2)
    print '[X] Done'
    print 'method.delivery_tag %s' % method.delivery_tag


if __name__ == '__main__':
    credentials = pika.PlainCredentials('mango', 'mango')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    channel = connection.channel()
    # 在我这个消费者当前消息还没处理完的时候就不要再给我发新消息了。
    channel.basic_qos(prefetch_count=1)
    channel.queue_declare(queue='task_queue')
    channel.basic_consume(callback, queue='task_queue', no_ack=True)
    print '[*] Waiting for message. To exit press CTRL+C'
    channel.start_consuming()
