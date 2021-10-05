# consumer.py
# Consume RabbitMQ queue
import pika
import json

class Queueworker():
    def __init__(self,siz):
        self.siz = siz
        self.count = 0

    def consume(self,q):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials("user", "password")))
        channel = connection.channel()

        def callback(ch, method, properties, body):
            self.count = self.count+1
            body = body.decode('utf-8')
            print(body)
            body = json.loads(body)
            q.append(body)
            if(self.count==self.siz):
                connection.close()

        channel.basic_consume(queue="output", on_message_callback=callback, auto_ack=True)
        channel.start_consuming()

    def produce(self,X,Y,i,server):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password')))
        channel = connection.channel()
        arr = [X,Y,i]
        json_string = json.dumps(arr)
        channel.basic_publish(exchange='output_exchange', routing_key=server, body=json_string)
        connection.close()




