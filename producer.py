from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

conf = {
    'bootstrap.servers': 'localhost:9092',  # Change to your Kafka broker address if needed
}

producer = Producer(conf)

# Produce a message to the 'test' topic
topic = 'test'
message = 'Hello, Kafka!'

producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
producer.flush()
