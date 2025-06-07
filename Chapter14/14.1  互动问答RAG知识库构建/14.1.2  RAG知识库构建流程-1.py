#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/24 17:10
# @Author  : yongjie.su
# @File    : 14.1.2  RAG知识库构建流程-1.py
# @Software: PyCharm
# 加载文档
from langchain_community.document_loaders import TextLoader

loader = TextLoader('dataset/data.txt')
documents = loader.load()

# 文档切分
from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=256,
    chunk_overlap=20,
    length_function=len,
)

texts = text_splitter.split_documents(documents)
print(texts[0])

# 创建词嵌入
from langchain_community.embeddings import HuggingFaceEmbeddings


def get_embeddings(bge_small_model_name="bge-base-zh"):
    embeddings = HuggingFaceEmbeddings(model_name=bge_small_model_name)
    return embeddings


embeddings = get_embeddings()

# 写入向量数据库
from langchain_community.vectorstores.faiss import FAISS

vetcor_store = FAISS.from_documents(texts, embedding=embeddings)
vec_path = "rag_vec.db"
vetcor_store.save_local(vec_path)
