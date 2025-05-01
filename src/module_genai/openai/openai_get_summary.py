import json
from openai import OpenAI
import models.output as o
import os

def openai_get_summary(articles):
    # will not work api key not available
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    MODEL_NAME = os.environ.get("OPENAI_MODEL")

    chat_messages = [
        {
            "role": "system", 
            "content": """
            Your role is to take a list of New York Times articles and return a summary of that days news.
            Return a JSON formatted response with keys: 
            "date": (str), 
            "summary": (str), 
            "top_story: (dict with "headline" and "summary"),
            "other_top_stories": (list of dicts with "headline" and "summary"),
            "topics": (list of dicts with "topic" and list of dicts with "headline" and "summary")
            """
        },
        {
            "role": "user", 
            "content": f"""
            Articles below delimited by back ticks are in JSON format with keys \"headline\" and \"summary.\" 
            ``` 
            {articles}
            """
        }
    ]
    response = client.chat.completions.create(
        model = MODEL_NAME,
        max_completion_tokens = 3300,
        temperature = 0.6,
        messages = chat_messages,
    )

    return response.choices[0].message.content

    # To Do -- Structured Outputs
    # response = client.responses.parse(
    #     model = MODEL_NAME,
    #     input = chat_messages,
    #     text_format = o.SummaryOutput
    # )

    # return json.dumps(response.output_parsed.__dict__)
