#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/24 11:59
# @Author  : yongjie.su
# @File    : 4.4.1 使用数据集生成Embedding.py
# @Software: PyCharm
import pandas as pd
from transformers import AutoModel


class EnglishEmbeddingLoader:
    def __init__(self, model_name):
        self._model_name = model_name
        self.model = self.load_model()

    def load_model(self):
        return AutoModel.from_pretrained(self._model_name, trust_remote_code=True)

    def get_embedding(self, sentence, max_length=768):
        sentence = sentence.strip().replace("\n", "")
        embedding = self.model.encode(sentence, max_length=max_length)
        return list(embedding)


if __name__ == '__main__':
    # Reviews_head_1000.csv 文件是 Reviews.csv 的前1000行小数据集
    file_name = "Reviews_head_1000.csv"
    # 载入数据
    df = pd.read_csv(file_name)
    # jinaai:jina-embeddings-v2-base-en 在 HuggingFace 上下载
    model_name = 'jinaai:jina-embeddings-v2-base-en'
    en_embd_loader = EnglishEmbeddingLoader(model_name)
    df['ada_embedding'] = df['Text'].apply(lambda line: en_embd_loader.get_embedding(line))
    df.to_csv('Reviews_embeddings.csv', index=False, header=True)
