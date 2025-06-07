#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/6 22:43
# @Author  : yongjie.su
# @File    : 8.4.1  链的定义.py
# @Software: PyCharm
from langchain_openai import AzureChatOpenAI

azure_endpoint = "https://internal-xxx.openai.azure.com/"
# azure 官网获取
openai_api_key = "eeexxx"

llm = AzureChatOpenAI(
    azure_endpoint=azure_endpoint,
    azure_deployment="gpt-35-turbo",
    openai_api_version="2024-02-15-preview",
    openai_api_key=openai_api_key)

from langchain_core.prompts import PromptTemplate

template = """
    请帮我进行计算：{a} + {b} 的值是多少？
"""
prompt = PromptTemplate(template=template, input_variables=["a", "b"])

from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)

output = chain.invoke(dict(a=1, b=2))
print(output)
