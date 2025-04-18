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
        system = """Your role is to take a list of New York Times articles and return a summary of that days news.
        Return a JSON formatted document with the keys
        {
            \"summary\":\"An overall summary of the days news\"
            \"top_story\":{\"headline\":\"article headline\",\"summary\":\"brief summary of the article\"}
            \"other_top_stories\":[{\"headline\":\"article headline\",\"summary\":\"brief summary of the article\"}]
            \"other_stories\": [{\"topic\": [\"headline\"]}]
        }
        """,
        messages=chat_messages
    )

    print(response.json())