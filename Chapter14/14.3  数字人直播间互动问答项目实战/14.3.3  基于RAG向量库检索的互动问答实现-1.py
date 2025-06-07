#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/29 22:46
# @Author  : yongjie.su
# @File    : 14.3.3  基于RAG向量库检索的互动问答实现-1.py
# @Software: PyCharm
from langchain_community.embeddings import HuggingFaceEmbeddings


def get_embeddings(bge_small_model_name="bge-base-zh"):
    embeddings = HuggingFaceEmbeddings(model_name=bge_small_model_name)
    return embeddings


embeddings = get_embeddings()

# 加载向量库
from langchain_community.vectorstores.faiss import FAISS

vec_path = "rag_vec.db"
faiss = FAISS.load_local(vec_path, embeddings)


def get_similarity_search(question, k=3):
    top3_results = faiss.similarity_search(question, k=k)
    return top3_results
