import os
import openai
from dotenv import load_dotenv
# openai.api_key = "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"
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]
# openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="what is python",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
chatbot_response = response.choices[0].text.strip()
print(chatbot_response)