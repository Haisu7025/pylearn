import pika
import random

credentials = pika.PlainCredentials('guest', 'geust')
parameters = pika.ConnectionParameters('localhost', 7888, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# channel.queue_declare(queue='hello')
number = random.randint(1, 1000)
body = 'hello world:%s' % number
channel.basic_publish(exchange='', routing_key='hello', body=body)
print " [x] Sent %s" % body
connection.close()
