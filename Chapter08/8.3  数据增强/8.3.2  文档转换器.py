#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/6 11:35
# @Author  : yongjie.su
# @File    : 8.3.2  文档转换器.py
# @Software: PyCharm

# 按字符切割器
# from langchain.text_splitter import CharacterTextSplitter
#
# texts = [
#     "这是一个按字符切割的测试数据",
#     "这是一个按字符切割的测试数据"
# ]
# text_splitter = CharacterTextSplitter(
#     chunk_size=512,
#     chunk_overlap=10
# )
# docs = text_splitter.create_documents(texts)
# print(docs)

# 递归按字符分割器
from langchain.text_splitter import RecursiveCharacterTextSplitter

with open("三国演义.txt", "r") as f:
    content = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1024,
    chunk_overlap=10,
    length_function=len,
    is_separator_regex=False,
)
docs = text_splitter.create_documents([content])
print(docs[0])
print(docs[1])
