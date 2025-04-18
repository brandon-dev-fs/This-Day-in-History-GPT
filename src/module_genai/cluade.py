from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()

# will not work api key not available
client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

MODEL_NAME = os.environ.get("ANTHROPIC_MODEL")

response = client.messages.create(
    model=MODEL_NAME,
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Write a haiku about Anthropic"}
    ],
)

print(response.content[0].text)
