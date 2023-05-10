import pika, json, os, django
from django.conf import settings

settings.configure()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

rabbitmq_host = "192.168.1.44"  # IP of your local machine
username = "admin"
password = "admin"
params = pika.URLParameters(f'amqp://{username}:{password}@{rabbitmq_host}:5672')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    from products.models import Product
    print('Received main')
    data = json.loads(body)
    print(data)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')

    """
    According to [0], queue is the name of the queue to consume from. If the empty string is used, the most recent 
    server-named queue for this channel will be used.
    
    on_message_callback is a function that will be called when consuming a message. It has the signature 
    on_message_callback(channel, method, properties, body), where channel is the pika.channel.Channel object, method is 
    the pika.spec.Basic.Deliver object, properties is the pika.spec.BasicProperties object, and body is the message body 
    as bytes.
    
    auto_ack is a boolean that determines whether automatic acknowledgement mode will be used. If set to True, the consumer 
    will automatically acknowledge the messages it receives. [0]
    
    In summary, channel.basic_consume() sets up a consumer to receive messages from a specified queue, and provides a
     callback function to handle those messages. The auto_ack parameter determines whether the consumer will automatically 
     acknowledge the messages. [0]"""


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
