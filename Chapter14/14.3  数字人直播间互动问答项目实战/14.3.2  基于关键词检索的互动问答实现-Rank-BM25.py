#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/28 00:12
# @Author  : yongjie.su
# @File    : 14.3.2  基于关键词检索的互动问答实现-Rank-BM25.py
# @Software: PyCharm
import jieba
from rank_bm25 import BM25Okapi

corpus = [
    "我们发顺丰快递。",
    "我们的包裹是从北京发货的。",
    "我们的商品都是有正品保障的，支持七天无理由退换货。",
    "护手霜男女生都适用，适用效果非常好。",
]

tokenized_corpus = [jieba.lcut_for_search(doc) for doc in corpus]

bm25 = BM25Okapi(tokenized_corpus)

query = "快递？"
tokenized_query = jieba.lcut_for_search(query)

doc_scores = bm25.get_scores(tokenized_query)
print(doc_scores)

results = bm25.get_top_n(tokenized_query, corpus, n=1)
print(results)
