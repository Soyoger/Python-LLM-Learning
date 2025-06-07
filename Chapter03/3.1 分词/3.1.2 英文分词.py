#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/24 20:32
# @Author  : yongjie.su
# @File    : 3.1.2 英文分词.py
# @Software: PyCharm

simple_example = "Tokenization is a crucial step in natural language processing."
simple_tokens = simple_example.split(" ")
print(simple_tokens)

# 可以放在代码里面执行
# import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize

nltk_example = "Tokenization is a crucial step in natural language processing."
nltk_tokens = word_tokenize(nltk_example)
print(nltk_tokens)

from nltk.corpus import stopwords

# 过滤停用词
filtered_tokens = [token for token in nltk_tokens if token not in stopwords.words('english')]
print(filtered_tokens)
