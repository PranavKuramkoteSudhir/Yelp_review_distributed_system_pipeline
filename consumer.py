import streamlit as st
from kafka import KafkaConsumer
import json
import pandas as pd

# Define Kafka consumer for 'order_detail' topic
order_detail_consumer = KafkaConsumer('order_detail', bootstrap_servers='localhost:29092', value_deserializer=json.loads)

# Define Kafka consumer for 'sentiment_analysis' topic
sentiment_analysis_consumer = KafkaConsumer('sentiment_analysis', bootstrap_servers='localhost:29092', value_deserializer=json.loads)

# Define DataFrame columns
order_detail_columns = ['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'text', 'date', 'category']
sentiment_analysis_columns = ['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'text', 'date', 'category', 'user_sentiment_rating']

# Streamlit app
st.title("Merged Data Display")

# Continuously update Streamlit with new messages from both topics
while True:
    order_detail_df = pd.DataFrame(columns=order_detail_columns)
    sentiment_analysis_df = pd.DataFrame(columns=sentiment_analysis_columns)

    for message in order_detail_consumer:
        value = message.value
        new_row = pd.DataFrame([value])
        order_detail_df = pd.concat([order_detail_df, new_row], ignore_index=True)

    for message in sentiment_analysis_consumer:
        value = message.value
        new_row = pd.DataFrame([value])
        sentiment_analysis_df = pd.concat([sentiment_analysis_df, new_row], ignore_index=True)

    # Merge data from both DataFrames based on a common key (e.g., 'review_id')
    merged_df = pd.merge(order_detail_df, sentiment_analysis_df, on='review_id', how='outer')

    # Display merged DataFrame in Streamlit
    st.write("Merged DataFrame:")
    st.write(merged_df)
