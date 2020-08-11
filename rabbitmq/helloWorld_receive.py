import pika

# receive a single  message to the queue

# establish connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create a queue to which message will be delivered:
channel.queue_declare(queue='hello')


# callback function
def callback(ch, method, properties, body):
    print(f' [x] Received {body}')


# consume message from the queue
channel.basic_consume(
    queue = 'hello',
    auto_ack = True,
    on_message_callback=callback
)

# never ending loop - waits for data and run callbacks whenever necessary
print(f' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


