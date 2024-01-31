# Yelp_review_kafka_pipeline_live_analysis
<img width="1239" alt="Screenshot 2024-01-31 at 9 32 35 AM" src="https://github.com/PranavKuramkoteSudhir/Yelp_review-Real-Time-Data-Streaming-/assets/139109363/deb4a26c-9331-4c9d-a9a4-ebf8e8b6a980">

-Yelp review data, including review ID, user ID, text, rating, and date, is initially collected.
-This data is streamed into a Kafka topic named reviews_db using a Kafka producer.
-Another component conducts sentiment analysis using the GPT-3.5 Turbo model on the data from reviews_db.
-GPT-3.5 Turbo generates sentiment ratings for each review, assessing the sentiment expressed in the text.
-The sentiment analysis results, along with the original review data, are sent to a separate Kafka topic named sentiment_analysis.
-A Kafka consumer retrieves messages from both reviews_db and sentiment_analysis.
-The consumer processes the messages, extracting review data and sentiment analysis results.
-Extracted review data is stored in a PostgreSQL database, maintaining data integrity and consistency.
-Tables such as reviews and sentiments in the PostgreSQL database capture the review details and sentiment analysis results.
-Tableau visualizations connected to the database provide insights into sentiment trends, distribution across categories, and user ratings.
