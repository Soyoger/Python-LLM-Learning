#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/21 22:35
# @Author  : yongjie.su
# @File    : 4.3.1 ChatGPT生成Embedding.py
# @Software: PyCharm
from openai import OpenAI

OPENAI_API_BASE = "https://api.openai-proxy.org/v1"
OPENAI_API_KEY = "sk-e44xxx"
if OPENAI_API_BASE is None or OPENAI_API_BASE == "":
    OPENAI_API_BASE = f"https://api.openai.com/v1"
client = OpenAI(
    base_url=OPENAI_API_BASE,
    api_key=OPENAI_API_KEY
)

if __name__ == "__main__":
    response = client.embeddings.create(
        input="输入的文本内容",
        model="text-embedding-ada-002"
    )
    # 结果转成json字符串格式
    print(response.model_dump_json())
    # 获取embedding
    embedding = response.data[0].embedding
    print(len(embedding))
    print(embedding)
