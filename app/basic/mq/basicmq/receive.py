# _*_coding:utf-8_*_
__author__ = 'mango'
import pika


def callback(channel, method, properties, body):
    print method
    print '[X] Recieved %r ' % body


if __name__ == '__main__':
    credentials = pika.PlainCredentials('mango', 'mango')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello')
    channel.basic_consume(callback, queue='hello', no_ack=True)
    print '[*] Waiting for message. To exit press CTRL+C'
    channel.start_consuming()
