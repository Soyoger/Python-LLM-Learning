#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/14 19:04
# @Author  : yongjie.su
# @File    : 3.3.2 基于BERT预训练模型-英文分词.py
# @Software: PyCharm
from loguru import logger
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-cased")

# from transformers import AutoTokenizer
# tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
sentence = "This model is case-sensitive: it makes a difference between english and English."
logger.info(f"原始句子：{sentence}")

# 获取分词Tokens
tokens = tokenizer.tokenize(sentence)
logger.info(f"分词Tokens：{tokens}")

# 编码：将Token映射为ID
ids = tokenizer.convert_tokens_to_ids(tokens)
logger.info(f"Tokens映射为Ids的结果：{ids}")


# 将ID映射为Token
tokens = tokenizer.convert_ids_to_tokens(ids)
logger.info(f"Ids映射为Tokens的结果：{tokens}")

# 解码还原原始句子
new_sentence = tokenizer.decode(ids)
logger.info(f"通过Ids解码还原原始句子：{new_sentence}")
#  解码还原原始句子
new_sentence = tokenizer.convert_tokens_to_string(tokens)
logger.info(f"通过Tokens解码还原原始句子：{new_sentence}")
