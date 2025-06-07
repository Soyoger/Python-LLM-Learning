#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/6 12:49
# @Author  : yongjie.su
# @File    : 8.3.3  文本嵌入.py
# @Software: PyCharm
from langchain_community.embeddings import HuggingFaceEmbeddings

# moka-ai/m3e-base 在Hugging Face官网下载
model_name = "moka-ai/m3e-base"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)
texts = [
    "这是一个按字符切割的测试数据",
    "这是一个按字符切割的测试数据"
]
# 生成文本嵌入
embed = embeddings.embed_documents(texts)
print(f"嵌入的长度：{len(embed[0])}")
print(embed)

# 生成查询嵌入
query = embeddings.embed_query("测试")
print(f"嵌入的长度：{len(query)}")
print(query)
