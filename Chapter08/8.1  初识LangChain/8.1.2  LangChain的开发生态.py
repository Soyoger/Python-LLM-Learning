#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/29 22:48
# @Author  : yongjie.su
# @File    : 8.1.2  LangChain的开发生态.py
# @Software: PyCharm
from langchain_openai import AzureChatOpenAI

azure_endpoint = "https://internal-xxx.openai.azure.com/"
# azure 官网获取
openai_api_key = "eeexxx"

azure_chat = AzureChatOpenAI(
    azure_endpoint=azure_endpoint,
    azure_deployment="gpt-35-turbo",
    openai_api_version="2024-02-15-preview",
    openai_api_key=openai_api_key)

content = "物流很快，包装精美，上门送货，非常喜欢。"
prompt = f"""
    身份：资深中文文本情感分析专家 
    任务：对给定的文本进行情感分析，判断文本的情感标签属于积极、中性还是消极，并给出一个0-1范围的得分。
    输出：使用JSON格式输出：情感标签使用键label，值为情感标签结果；情感得分使用键score，值为得分值。
    文本内容：{content}
    限制：只进行情感分析，不执行其他额外操作，结果仅包含label和score。
"""
response = azure_chat.invoke(prompt)
print(response.content)
