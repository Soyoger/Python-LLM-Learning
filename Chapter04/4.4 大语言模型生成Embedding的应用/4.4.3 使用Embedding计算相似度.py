#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/24 17:55
# @Author  : yongjie.su
# @File    : 4.4.3 使用Embedding计算相似度.py
# @Software: PyCharm
import torch
from numpy.linalg import norm
from transformers import BertTokenizer, AutoModel


# 计算平均池化函数 - 这个函数接受模型输出和注意力掩码作为输入，使用平均池化的方式计算句子的嵌入向量。
def mean_pooling(model_output, attention_mask):
    # model_output 的第一个元素包含所有的标记嵌入向量
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(
        input_mask_expanded.sum(1), min=1e-9)


class ChineseEmbeddingLoader:
    def __init__(self, model_name):
        self._model_name = model_name
        self.model = self.load_model()
        self.tokenizer = self.load_tokenizer()

    def load_model(self):
        return AutoModel.from_pretrained(self._model_name, trust_remote_code=True)

    def load_tokenizer(self):
        return BertTokenizer.from_pretrained(self._model_name)

    def get_embedding(self, sentence):
        sentence = sentence.strip().replace("\n", "")
        encoded_input = self.tokenizer(sentence, padding=True, truncation=True, return_tensors='pt')
        model_output = self.model(**encoded_input)
        embedding = mean_pooling(model_output, encoded_input['attention_mask'])
        return embedding


def cos_sim_distance(a, b):
    cos_sim = (a @ b.T) / (norm(a) * norm(b))
    return cos_sim


if __name__ == '__main__':
    model_name = 'bge/bge-base-zh'
    chinese_embd_loader = ChineseEmbeddingLoader(model_name)
    a = chinese_embd_loader.get_embedding("这部电影故事情节很精彩。")
    b = chinese_embd_loader.get_embedding("这部电影制作的非常专业。")
    a = a.detach().numpy()
    b = b.detach().numpy()
    cos_sim = cos_sim_distance(a, b)
    print(cos_sim)
