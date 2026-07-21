import time

from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import datetime

from agent.agent import generate_test_script
from evaluator.code_evaluator import evaluate_code
from evaluator.execution_evaluator import execute_test_script

load_dotenv()

#link deepseek llm
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)

#link deepseek llm
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
                  "total_tokens": response.usage.total_tokens,
                  "timestamp": datetime.datetime.now().isoformat()
                  }
    except Exception as e:
        return {"status": "FAIL",
                "prompt": prompt,
                "error": str(e)
                }

#load testcases from json file
def load_testcases(file_path):
    with open(file_path,"r",encoding="utf-8") as f:
        testcases = json.load(f)
    return testcases

#run testcase
def run_testcases(testcases):
    results = []
    for testcase in testcases:
        print(f"Running {testcase['id']}.......")
        result = call_llm(testcase["prompt"])
        result["testcase_id"] = testcase.get("id","unknown")
        results.append(result)
    return results

#run generate testcase
def run_generate_testcases(testcases):
    results = []
    for testcase in testcases:
        print(f"Running {testcase['id']}.......")
        script = generate_test_script(testcase["requirement"])
        evaluation = evaluate_code(script,testcase["requirement"])
        execution = execute_test_script(script)
        result = {
            "testcase_id": testcase.get("id","unknown"),
            "requirement": testcase.get("requirement","unknown"),
            "generated_script": script,
            "evaluation": evaluation,
            "execution": execution
        }
        results.append(result)
    return results



if __name__ == "__main__":
    testcases = load_testcases("./testcases/network_cases.json")
    #results = run_testcases(testcases)
    results = run_generate_testcases(testcases)
    for result in results:
        print("=" * 60)
        print("Testcase:")
        print(result["testcase_id"])
        print("\nRequirement:")
        print(result["requirement"])
        print("\nGenerated Script:")
        print(result["generated_script"])
        print("\nEvaluation:")
        print(result["evaluation"])
        print("\nExecution:")
        print(result["execution"])