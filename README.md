# Kafka with Docker and Python Demo

Source: [YouTube Video](https://www.youtube.com/watch?v=LHNtL4zDBuk&list=PLQ5j-FTc2VhAY_PBg7FVkZsal50MCgp7Y&index=3)

## Spin up Zookeeper and Kafka using docker-compose
```docker-compose -f docker-compose.yml up -d```

## Check both Zookeeper and Kafka are up and running
```docker ps```

## Enter Kafka container shell and create a new topic
```docker exec -it kafka /bin/sh```  
```cd opt/kafka_2.13-2.8.1/bin```  
```kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic messages```  

## Create a new Python project in Pycharm, install kafka-python
```pip install kafka-python```

## Start Kafka producer
Open a PyCharm terminal.
```python producer.py```

## Start Kafka consumer
Open a different PyCharm terminal.
```python consumer.py```