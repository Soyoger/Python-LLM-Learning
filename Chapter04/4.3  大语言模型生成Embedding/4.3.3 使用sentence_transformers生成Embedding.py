#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/22 14:01
# @Author  : yongjie.su
# @File    : 4.3.3 使用sentence_transformers生成Embedding.py
# @Software: PyCharm
from sentence_transformers import SentenceTransformer


def get_embedding_by_sentence_transformers(model_name):
    model = SentenceTransformer(model_name_or_path=model_name)
    return model


if __name__ == '__main__':
    model_name = "shibing624_text2vec-base-chinese"
    model = get_embedding_by_sentence_transformers(model_name)
    embedding = model.encode("这是单条文本的例子。")
    print(embedding)
    embeddings = model.encode(["这是多文本例子的第一条。", "这是多文本例子的第二条。"])
    print(embeddings)
