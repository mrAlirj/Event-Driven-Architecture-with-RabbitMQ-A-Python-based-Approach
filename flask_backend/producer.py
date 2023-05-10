import pika, json

rabbitmq_host = "192.168.1.44"  # IP of your local machine
username = "admin"
password = "admin"
params = pika.URLParameters(f'amqp://{username}:{password}@{rabbitmq_host}:5672')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
