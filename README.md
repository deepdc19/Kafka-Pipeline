# Kafka-Pipeline
The project explores the implementation of a Kafka-based pipeline for the ingestion of data sourced
from the News API. The pipeline utilizes Kafka producers to transmit the acquired data to consumers.
Within the producer, data is parsed before being dispatched to the consumer, which subsequently stores
the processed data in a CSV format. This stored CSV file is intended for integration into a Hive table
for further analysis. Moreover, the CSV file is migrated to the Hadoop Distributed File System
(HDFS), where it is employed by a Hive table to facilitate comprehensive data analysis. Through this
pipeline architecture, the study endeavors to streamline the real-time ingestion and analysis of data
sourced from the News API, ultimately facilitating insights and decision-making processes.
