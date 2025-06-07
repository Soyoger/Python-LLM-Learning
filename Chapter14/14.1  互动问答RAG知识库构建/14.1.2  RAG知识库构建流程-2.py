#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/24 17:31
# @Author  : yongjie.su
# @File    : 14.1.2  RAG知识库构建流程-2.py.py
# @Software: PyCharm
# 创建词嵌入
from langchain_community.embeddings import HuggingFaceEmbeddings


def get_embeddings(bge_small_model_name="bge-base-zh"):
    embeddings = HuggingFaceEmbeddings(model_name=bge_small_model_name)
    return embeddings


embeddings = get_embeddings()

# 加载向量库
from langchain_community.vectorstores.faiss import FAISS

vec_path = "rag_vec.db"

faiss = FAISS.load_local(vec_path, embeddings)


# 检索
def get_similarity_search(question, k=3):
    top3_results = faiss.similarity_search(question, k=k)
    return top3_results


question = "护手霜怎么使用？"
top3_results = get_similarity_search(question)
page_contents = [top3_result.page_content for top3_result in top3_results]

print(top3_results)

# 内容生成
prompt_template = """
# 角色
电商平台数字人直播互动问答台词撰写专家，能够根据核心关键词及附加信息撰写互动问答台词。

# 技能
    - 擅长根据问答信息撰写互动问答台词，语调温馨，逻辑性强
    - 精通中文，有良好的中文阅读与理解能力
    - 深谙电商数字人直播的运营流程与互动问答场景
    - 掌握Markdown语法，能够准确识别和处理相关信息

# 问答信息
    问答开头：我看到 "昵称" 关于 "关键词" 的问题了，
    关键词：{keyword}
    问题分类：{category}
    附加信息：{context}

# 输出要求
    - 根据问答信息撰写直播间互动问答的台词
    - 所有台词不能包括敏感词库里面的任何一个字词
    - 输出结果的字数限制在50字以内。
    - 只输出与该商品相关的信息，其他信息自动忽略

# 敏感词库

    敏感词：世界级、最高级、第一、唯一、首个、最好、最便宜、美白、祛痘
"""
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(prompt_template)

keyword = "护手霜、使用方法"
category = "护手霜使用方法"
context = "\n".join(page_contents)

prompt = prompt.format(
    keyword=keyword,
    category=category,
    context=context
)

import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"
from langchain_openai import AzureChatOpenAI

azure_endpoint = "https://internal-qa-service-branch2.openai.azure.com/"
openai_api_key = "eeexxx"

azure_chat = AzureChatOpenAI(
    azure_endpoint=azure_endpoint,
    azure_deployment="gpt-35-turbo",
    openai_api_version="2024-02-15-preview",
    openai_api_key=openai_api_key)

response = azure_chat.invoke(prompt)
print(response.content)
