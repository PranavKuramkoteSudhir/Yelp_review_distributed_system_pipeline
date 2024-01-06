import json
import time
from kafka import KafkaProducer

from get_data import review_get
from user_data import get_user

ORDER_KAFKA_TOPIC = "order_detail"
ORDER_LIMIT = 50

producer = KafkaProducer(bootstrap_servers="localhost:29092")

print("Going to be generating order after 10 seconds")
print("Will generate one unique order every 5 seconds")
time.sleep(10)
count=0
for i in range(ORDER_LIMIT):
    data = review_get(count)
    count+=1
    producer.send(ORDER_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
    print(f"Done Sending..{i}")
    time.sleep(5)