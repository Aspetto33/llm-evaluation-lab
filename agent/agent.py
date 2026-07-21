
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL"),
)

def generate_test_script(requirement):
    prompt = f"""
你是一名网络自动化测试专家。

请根据下面需求生成Python pytest测试脚本。

要求：
1. 文件可以直接pytest执行
2. 包含测试步骤
3. 必须包含assert
4. 至少包含一个test_xxx函数


需求：

{requirement}

只输出代码，不要解释。
"""
    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {
                "role" : "user",
                "content" : prompt
            }
        ]
    )
    return response.choices[0].message.content