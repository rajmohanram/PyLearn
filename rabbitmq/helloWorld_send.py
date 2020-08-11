import pika

# send a single  message to the queue

# establish connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create a queue to which message will be delivered:
channel.queue_declare(queue='hello')

# message: body
body = "Welcome to the world of AMPQ messaging."
# send message to the queue through an exchange
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body=body
)

print(f" [x] Sent Message !")

# close the connection
connection.close()
