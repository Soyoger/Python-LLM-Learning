#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/11 17:46
# @Author  : yongjie.su
# @File    : 3.3.2 基于BERT预训练模型-中文分词.py
# @Software: PyCharm
from transformers import BertTokenizer
# bert-base-chinese 在Hugging Face 或者 ModelScope 官网下载
tokenizer = BertTokenizer.from_pretrained("bert-base-chinese")

# from transformers import AutoTokenizer
# tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
sentence = "2023年度十大新词语是：生成式人工智能、全球文明倡议、村超、新质生产力、全国生态日、消费提振年、特种兵式旅游、显眼包、百模大战、墨子巡天。"

tokens = tokenizer.tokenize(sentence)
print(tokens)
print(tokenizer(sentence))
# 将token 映射为ID
ids = tokenizer.convert_tokens_to_ids(tokens)
print(ids)
# 输出分词结果
tokens = tokenizer.convert_ids_to_tokens(ids)
print(tokens)
# 解码
decoder = tokenizer.decode(ids)
print(decoder)
