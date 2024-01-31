import random

import pandas as pd
import json


file_path="/Users/pranav/Desktop/linux_test/kafka_attempt02/dataset/yelp_academic_dataset_review.json"
def review_get(last_sent_index):
    try:
        with open(file_path, 'r') as file:
            # skip the lines that were already sent
            for _ in range(last_sent_index):
                next(file)

            # Read a line from the file
            line = file.readline()
            cat_list = ["Fast food", "Restaurant", "Site seeing", "Historic site", "activity", "Show"]
            # Check if there is a line to process
            if line:
                records = json.loads(line)
                df = pd.DataFrame([records])  # Convert list of dictionary to DataFrame

                # Convert integer values to native Python integers
                result = {
                    "review_id": df['review_id'].iloc[0],
                    "user_id": df['user_id'].iloc[0],
                    "business_id": df['business_id'].iloc[0],
                    "stars": int(df['stars'].iloc[0]),
                    "useful": int(df['useful'].iloc[0]),
                    "funny": int(df['funny'].iloc[0]),
                    "cool": int(df['cool'].iloc[0]),
                    "text": df['text'].iloc[0],
                    "date": df['date'].iloc[0],
                    "category": cat_list[random.randint(0,len(cat_list))]
                }

                last_sent_index += 1
                return result
            else:
                print("No more lines to read.")
                return None

    except Exception as e:
        print(e)
        return None