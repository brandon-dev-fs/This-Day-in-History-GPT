from anthropic import Anthropic
import os

def claude_get_summary(articles):
    # will not work api key not available
    client = Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY")
    )

    MODEL_NAME = os.environ.get("ANTHROPIC_MODEL")

    chat_messages = [
        {
            "role": "user", 
            "content": f"""
            Articles below delimited by back ticks are in JSON format with keys \"headline\" and \"summary.\" 
            Review the articles and return the following
            A JSON formatted response with keys: "date": (str), "summary": (str), "top_story: (dict with "headline" and "summary"), "other_top_stories": (list of dicts with "headline" and "summary"), "topics": (list of dicts with "topic" and list of dicts with "headline" and "summary")
            ``` 
            {articles}
            """
        }
    ]

    response = client.messages.create(
        model = MODEL_NAME,
        max_tokens = 4000,
        temperature = 0.0,
        system="Your role is to take a list of New York Times articles and return a summary of that days news. Take into account historical context and impact articles may have on today.",
        messages = chat_messages
    )

    res_text = response.content[0].text

    return res_text.split("json")[1] if res_text.find("json") > -1 else res_text # return content always starts with ```json
