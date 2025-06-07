#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 21:44
# @Author  : yongjie.su
# @File    : 14.2.2  文档分块策略优化.py
# @Software: PyCharm
# 按固定大小分块
from langchain.text_splitter import CharacterTextSplitter

text = "超大大文本内容"
text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=256,
    chunk_overlap=20
)
docs = text_splitter.create_documents([text])
print(docs)

# 句子分块
import spacy
from spacy.lang.zh import Chinese

# 加载中文模型
nlp = Chinese()
# 添加句子分割器
nlp.add_pipe("sentencizer")


def sentence_chunking(text):
    """
    将文本分割成句子
    :param text: 输入文本
    :return: 包含句子的列表
    """
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    return sentences


text = "句子分块是一种基于自然语言结构的分块方法，特别适用于需要保留文本精确语义和上下文连贯性的应用场景。在句子分块中，文本被分割成一个个独立的句子，每个句子作为一个分块单元。这种方法确保了每个分块都能完整地表达其含义，不会因为被截断而丧失语义信息。"
chunks = sentence_chunking(text)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}: {chunk}")

# 递归分块

from langchain.text_splitter import RecursiveCharacterTextSplitter

text = "递归分块是一种高级文本分块方法，通过使用一组分隔符以分层和迭代的方式将输入文本分解成更小的块。"
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=256,
    chunk_overlap=20
)

docs = text_splitter.create_documents([text])
print(docs)
