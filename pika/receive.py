import pika

credentials = pika.PlainCredentials('guest', 'nova')
parameters = pika.ConnectionParameters('localhost', 7888, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)


channel.basic_consume(callback, queue='hello',   no_ack=True)

channel.start_consuming()
