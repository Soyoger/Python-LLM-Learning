#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/22 14:01
# @Author  : yongjie.su
# @File    : 4.3.2 使用text2vec生成Embedding.py
# @Software: PyCharm
"""
除了使用shibing624_text2vec-base-chinese
还可以尝试使用moka-ai/m3e-base、bge-base-zh

"""
from text2vec import SentenceModel, EncoderType


def get_embedding_by_text2vec(
        model_name_or_path, encoder_type=EncoderType.MEAN, max_seq_length=256, device="cpu"):
    model = SentenceModel(
        model_name_or_path=model_name_or_path,
        encoder_type=encoder_type,
        max_seq_length=max_seq_length,
        device=device
    )
    return model


if __name__ == '__main__':
    # shibing624_text2vec-base-chinese 在 HuggingFace 上下载
    model_name = "shibing624_text2vec-base-chinese"
    model = get_embedding_by_text2vec(model_name)
    embedding = model.encode("这是单条文本的例子。")
    print(embedding)
    embeddings = model.encode(["这是多文本例子的第一条。", "这是多文本例子的第二条。"])
    print(embeddings)
