#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/24 10:52
# @Author  : yongjie.su
# @File    : 4.3.4 使用transfomners库生成Embedding.py
# @Software: PyCharm
import torch
from transformers import BertTokenizer, BertModel


# 计算平均池化函数 - 这个函数接受模型输出和注意力掩码作为输入，使用平均池化的方式计算句子的嵌入向量。
def mean_pooling(model_output, attention_mask):
    # model_output 的第一个元素包含所有的标记嵌入向量
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(
        input_mask_expanded.sum(1), min=1e-9)


if __name__ == "__main__":
    # 从HuggingFace Hub下载到本地的模型路径
    model_name = "shibing624_text2vec-base-chinese"
    # 使用 BertTokenizer 加载了预训练的 BERT分词器，用于将输入的句子进行分词。
    tokenizer = BertTokenizer.from_pretrained(model_name)
    # 然后使用 BertModel 加载了预训练的 BERT 模型。
    model = BertModel.from_pretrained(model_name)
    # 准备输入的句子
    sentences = ['这是多文本例子的第一条。', '这是多文本例子的第二条。']

    # 使用分词器对句子进行分词处理，并进行填充和截断等预处理，返回编码后的输入。
    encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
    print(encoded_input)
    # 生成嵌入向量
    with torch.no_grad():
        model_output = model(**encoded_input)
    # 使用 mean_pooling 函数，将模型输出和注意力掩码作为输入，计算句子的嵌入向量。
    sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
    print(sentence_embeddings)
