#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/6 22:00
# @Author  : yongjie.su
# @File    : 8.3.5  检索器.py
# @Software: PyCharm
# 第一步，文本加载与转换
from langchain.text_splitter import RecursiveCharacterTextSplitter

with open("三国演义.txt", "r") as f:
    content = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=10,
    length_function=len,
    is_separator_regex=False,
)
docs = text_splitter.create_documents([content])

# 第二步，初始化文本嵌入
from langchain_community.embeddings import HuggingFaceEmbeddings

model_name = "moka-ai/m3e-base"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
hf_embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# 第三步，向量存储
from langchain_community.vectorstores import FAISS

db = FAISS.from_documents(docs, hf_embeddings)

# 获取检索器
retriever = db.as_retriever(search_type="similarity")
docs = retriever.get_relevant_documents("刘备三顾茅庐，与诸葛亮在隆中对中聊了什么？")
print(docs)
