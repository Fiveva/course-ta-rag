import os
import time
import json
import pandas as pd
import requests

API_URL = "https://api.dify.ai/v1/chat-messages"
API_KEY = os.environ["DIFY_API_KEY"]

INPUT_FILE = "evaluation_50.xlsx"
OUTPUT_FILE = "results_V1.xlsx"

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Test Cases",
    header=3
)

text_columns = [
    "V1_answer",
    "V1_notes",
    "conversation_id",
    "retriever_resources",
    "api_status"
]

for column in text_columns:
    if column not in df.columns:
        df[column] = ""
    else:
        df[column] = df[column].astype("object")
        df[column] = df[column].where(df[column].notna(), "")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

for index, row in df.iterrows():
    payload = {
        "inputs": {},
        "query": row["question"],
        "response_mode": "blocking",
        "conversation_id": "",
        "user": "course-agent-eval-V1"
    }

    start = time.time()

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=120
        )
        response.raise_for_status()
        result = response.json()

        df.at[index, "V1_answer"] = result.get("answer", "")
        df.at[index, "conversation_id"] = result.get("conversation_id", "")
        df.at[index, "latency_seconds"] = round(time.time() - start, 2)

        metadata = result.get("metadata", {})
        df.at[index, "retriever_resources"] = json.dumps(
            metadata.get("retriever_resources", []),
            ensure_ascii=False
        )

        usage = metadata.get("usage", {})
        df.at[index, "total_tokens"] = usage.get("total_tokens", "")
        df.at[index, "api_status"] = "success"

    except Exception as error:
        df.at[index, "api_status"] = "failed"
        df.at[index, "V1_notes"] = str(error)

    print(f"{index + 1}/{len(df)}：{row['test_id']}")
    time.sleep(1)

df.to_excel(OUTPUT_FILE, index=False)
print(f"评测完成：{OUTPUT_FILE}")