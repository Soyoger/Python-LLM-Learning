#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/24 11:31
# @Author  : yongjie.su
# @File    : test.py
# @Software: PyCharm
from sentence_transformers import SentenceTransformer
from transformers import AutoModel


def get_embedding_by_sentence_transformers(model_name):
    model = SentenceTransformer(model_name_or_path=model_name)
    return model


# 如果本地不存在，会自动远程下载
model = AutoModel.from_pretrained('jinaai:jina-embeddings-v2-base-en',
                                  trust_remote_code=True)  # trust_remote_code is needed to use the encode method
embeddings = model.encode(['How is the weather today?', 'What is the current weather like today?'])
print(embeddings)

# 相似度计算
# cos_sim = lambda a, b: (a @ b.T) / (norm(a) * norm(b))
# print(cos_sim(embeddings[0], embeddings[1]))

# embeddings = model.encode(
#     ['How is the weather today?'],
#     max_length=128
# )
# print(embeddings)
