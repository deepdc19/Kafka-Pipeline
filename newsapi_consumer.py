from kafka import KafkaConsumer
import json
import csv

#Broker configuration
bootstrap_servers = 'localhost:9092'
consumer = KafkaConsumer('project-newsapi-topic', bootstrap_servers=bootstrap_servers)

# csv file
csv_file_path = 'news_data.csv'

#Writing in CSV file as the data is received
with open(csv_file_path, 'w', newline='') as csv_file:
    # Setting CSV header
    csv_header = ['source', 'author', 'title', 'description', 'url', 'publishedAt', 'content']
    writer = csv.DictWriter(csv_file, fieldnames=csv_header)
    writer.writeheader()
    # Read messages from Kafka topic
    for message in consumer:
        message_data = json.loads (message.value)
        print("Message recieved from producer")
        writer.writerowmessage_data
        csv_file.flush()