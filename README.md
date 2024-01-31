# Yelp_review_kafka_pipeline_live_analysis
Real-time sentiment analysis of user comments using ChatGPT in a Streamlit app. 
Live updates from Kafka are displayed in a table with sentiment analysis results. Original data, sentiment, and other details are stored in PostgreSQL. 
Optimized for efficiency and integration.


This project involves real-time sentiment analysis of user comments using ChatGPT in a Streamlit application. Live updates are obtained from a Kafka topic ('order_detail'), displaying information such as review ID, user ID, business ID, stars, and category in a tabular format. The sentiment of user comments is analyzed using the ChatGPT model, and the results are integrated into the Streamlit UI. Additionally, the app connects to a PostgreSQL database for persistent storage, storing original user comments, sentiment analysis results, and other details. The project aims for efficiency in handling real-time data updates and seamless integration between Kafka, ChatGPT, Streamlit, and PostgreSQL.

<img width="1239" alt="Screenshot 2024-01-31 at 9 32 35 AM" src="https://github.com/PranavKuramkoteSudhir/Yelp_review-Real-Time-Data-Streaming-/assets/139109363/deb4a26c-9331-4c9d-a9a4-ebf8e8b6a980">
