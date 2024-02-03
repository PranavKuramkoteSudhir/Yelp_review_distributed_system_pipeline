from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
import pandas as pd
from sentiment_anlysis import sentiment_analysis_with_rating

# Define Kafka consumer and producer
consumer = KafkaConsumer('order_detail', bootstrap_servers='localhost:29092', value_deserializer=json.loads)
producer = KafkaProducer(bootstrap_servers="localhost:29092")

# Define DataFrame columns
columns = ['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'text', 'date', 'category']
df = pd.DataFrame(columns=columns)

# Continuously process messages
for message in consumer:
    value = message.value
    new_row = pd.DataFrame([value])
    df = pd.concat([df, new_row], ignore_index=True)

    # Perform sentiment analysis on the latest 'text' column
    df['user_sentiment_rating'] = sentiment_analysis_with_rating(df['text'])

    # Send sentiment analysis results to Kafka topic
    producer.send('sentiment_analysis', json.dumps(df.to_dict(orient='records')).encode("utf-8"))
