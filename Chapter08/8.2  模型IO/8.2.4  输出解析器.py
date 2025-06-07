#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 23:39
# @Author  : yongjie.su
# @File    : 8.2.4  输出解析器.py
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

# Json 格式
# from langchain_core.pydantic_v1 import BaseModel, Field
#
#
# class Output(BaseModel):
#     result: str = Field(description="结果")
#     remark: str = Field(description="备注")
#
#
# structured_llm = azure_chat.with_structured_output(Output, method="json_mode")
#
# prompt = f""""
#     功能：请判断1大于2吗？为什么？
#     输出：返回结果是或者否，并说明原因。结果用`result`，判断原因用`remark`键，以JSON形式响应。
#     限制：说明原因，限制在10个字以内。
#     """
# print(structured_llm.invoke(prompt))

# 结构化输出解析器
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import PromptTemplate

response_schemas = [
    ResponseSchema(name="answer", description="用户问题的答案"),
    ResponseSchema(
        name="result",
        description="结果",
    ),
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    template="请严谨的回答用户的问题。\n{format_instructions}\n{question}",
    input_variables=["question"],
    partial_variables={"format_instructions": format_instructions},
)
print(azure_chat.invoke("请判断1大于2吗？为什么？").content)
