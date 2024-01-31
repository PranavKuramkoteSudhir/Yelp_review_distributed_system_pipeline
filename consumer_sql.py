from kafka import KafkaConsumer
from sqlalchemy import create_engine, Table, MetaData
import json

# Kafka configuration
bootstrap_servers = 'localhost:29092'
group_id = 'my_consumer_group'
topics = ['reviews_db', 'sentiment_analysis']

# SQL database configuration
db_url = 'sqlite:///data.db'  # SQLite example, replace with your database URL

# Kafka consumer setup
consumer = KafkaConsumer(
    *topics,
    group_id=group_id,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# SQL database setup
engine = create_engine(db_url)
metadata = MetaData()
metadata.reflect(bind=engine)
reviews_table = Table('reviews', metadata, autoload=True, autoload_with=engine)
sentiment_table = Table('sentiments', metadata, autoload=True, autoload_with=engine)

# Main loop to consume messages
try:
    for message in consumer:
        topic = message.topic
        value = message.value
        
        if topic == 'reviews_db':
            # Insert data into reviews table
            with engine.connect() as connection:
                connection.execute(reviews_table.insert().values(value))
        
        elif topic == 'sentiment_analysis':
            # Insert data into sentiments table
            with engine.connect() as connection:
                connection.execute(sentiment_table.insert().values(value))

except KeyboardInterrupt:
    pass

finally:
    consumer.close()
