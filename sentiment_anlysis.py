import openai

def sentiment_analysis_with_rating(comment) -> float:
    if comment:
        openai.api_key = ""
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    "role": "system",
                    "content": """
                        You're a machine learning model with a task of providing a sentiment rating from 0 to 5.
                        Use a decimal value for more granularity, e.g., 3.5.
                        Here is the comment:

                        {comment}
                    """.format(comment=comment)
                }
            ]
        )

        # Directly return the sentiment rating
        return float(completion.choices[0].message['content'].strip())

    return 2.5  # Default to neutral for empty comments
