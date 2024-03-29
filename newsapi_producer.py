# -*- coding: utf-8 -*-
"""NewsAPI_Producer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ffU2vdapKws1BnooyM-NWesssbVT-8n1

# News API
This API can get news articles from different sources and different topics.

---


Documentation for Python API can be found at:
https://github.com/mattlisiv/newsapi-python
"""

'''
You do need to install following packages using pip package manager
pip install newsapi
pip install newsapi-python
pip install kafka-python
'''
from newsapi import NewsApiClient
import json
from kafka import KafkaProducer
from datetime import datetime

# Get your free API key from https://newsapi.org/, just need to sign up for an account
key = "fba1a511ddbb4db0a8fa8d7d3cc79f06"

# Initialize api endpoint
newsapi = NewsApiClient(api_key=key)

# Define the list of media sources
sources = 'bbc-news,cnn,fox-news,nbc-news,the-guardian-uk,the-new-york-times,the-washington-post,usa-today,independent,daily-mail'

# /v2/everything
all_articles = newsapi.get_everything(q='canada',
                                      sources=sources,
                                      language='en')
def parse_content(val):
    if val:
        return val.replace(',','')
    return ""

# Print the titles of the articles

for article in all_articles['articles']:
    if article['title'] != '[Removed]':
        print(article['title'])
        # Parsing the contents of the data
        del article['urlToImage']
        if article['publishedAt']:
            try:
                date = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:M:%SZ')
                article['publishedAt'] = date.timestamp()
            except ValueError as e:
                continue
        article['source'] = article['source']['name']
        article['description'] = parse_content(article['description'])
        article['author'] = parse_content (article['author'])
        article['title'] = parse_content(article['title'])
        article['content'] = parse_content(article['content']) 
        article['content'] = article['content'].replace("\n", '')
        article['content'] = article['content'].replace('\r', '')
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        producer.send('project-newsapi-topic', json.dumps(article).encode('utf-8'))