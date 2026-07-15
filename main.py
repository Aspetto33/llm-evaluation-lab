import time

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

#link deepseek llm
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)

def call_llm(prompt):
    try:
        start_time = time.perf_counter()
        # request and response
        response = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        latency = time.perf_counter() - start_time

        return   {"status": "PASS",
                  "prompt": prompt,
                  "answer": response.choices[0].message.content,
                  "latency": round(latency, 3),
                  "prompt_tokens": response.usage.prompt_tokens,
                  "completion_tokens": response.usage.completion_tokens,
                  "total_tokens": response.usage.total_tokens
                  }
    except Exception as e:
        return {"status": "FAIL",
                "prompt": prompt,
                "error": str(e)
                }

if __name__ == "__main__":
    result = call_llm("请解释一下mbist是什么")
    print(result)