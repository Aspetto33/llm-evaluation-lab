import time

from openai import OpenAI, base_url
from dotenv import load_dotenv
import os

load_dotenv()

#link deepseek llm
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)

start_time = time.perf_counter()

#request and response
response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {
            "role": "user",
            "content": "请解释一下mbist是什么"
        }
    ]
)

end_time = time.perf_counter()

latency = end_time - start_time

#print(response.choices[0].message.content)
#print(response.usage)
print(response)
print(latency)