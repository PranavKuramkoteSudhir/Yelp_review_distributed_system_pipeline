import streamlit as st
from kafka import KafkaConsumer
import json
import pandas as pd
import matplotlib.pyplot as plt

st.title("Live Updates from Kafka")

consumer = KafkaConsumer('order_detail', bootstrap_servers='localhost:29092', value_deserializer=json.loads)

columns = ['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'text', 'date', 'category']
df = pd.DataFrame(columns=columns)
plot_container = st.empty()
table_container = st.empty()


for message in consumer:
    value = message.value
    new_row = pd.DataFrame([value])
    df = pd.concat([df, new_row], ignore_index=True)

    # Group data based on 'category' and calculate the average stars
    avg_stars_by_category = df.groupby('category')['stars'].mean()

    # Display the table and plot
    table_container.table(df)
    plot_container.bar_chart(avg_stars_by_category)
