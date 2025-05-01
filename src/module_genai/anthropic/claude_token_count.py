from anthropic import Anthropic
import os

def claude_token_count(message):
    # will not work api key not available
    client = Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY")
    )

    MODEL_NAME = os.environ.get("ANTHROPIC_MODEL")

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
            "content": f"""Take the following list of articles delimited by back ticks, and summarize that days news in an easy to read summary. 
            Articles are in JSON format with keys \"headline\" and \"summary.\" 
            Highlight important articles based on their historical or societal impact.
            ``` {message}```
            """
        }
    ]

    response = client.messages.count_tokens(
        model=MODEL_NAME,
        messages=chat_messages
    )

    print(response.json())