from kafka import KafkaProducer
import json
from data_generator_2 import get_registered_user
import time

def json_serializer(message):
    return json.dumps(message).encode('utf-8')


producer = KafkaProducer(
           bootstrap_servers=['localhost:9092'],
           value_serializer=json_serializer,
)

if __name__ == '__main__':
    while True:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send("registered_user_2", registered_user)
        time.sleep(4)

