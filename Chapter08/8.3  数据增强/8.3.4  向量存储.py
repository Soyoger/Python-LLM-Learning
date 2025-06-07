#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/6 13:53
# @Author  : yongjie.su
# @File    : 8.3.4  向量存储.py
# @Software: PyCharm
# 第一步，准备文档
from langchain.text_splitter import CharacterTextSplitter

texts = [
    "这是苹果，很甜。",
    "这是梨，很脆。",
    "这是青橘，很酸。"
]
text_splitter = CharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=10
)
docs = text_splitter.create_documents(texts)

# 初始化文本嵌入
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
# 查看创建的向量ID
print(db.index_to_docstore_id)

# 添加文本
db.add_texts(["这是桃子"])
# 查看创建的向量ID
print(db.index_to_docstore_id)

# 按ID删除文档
db.delete(list(db.index_to_docstore_id.values())[:2])
print(db.index_to_docstore_id)

# 向量搜索
result = db.similarity_search("酸", k=2)
print(result)

# 检索器
retriever = db.as_retriever(search_type="mmr")
