#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 23:42
# @Author  : yongjie.su
# @File    : 14.2.5  重排序Rerank优化.py
# @Software: PyCharm

from FlagEmbedding import FlagReranker

# 构造一个FlagReranker实例，设置量化 use_fp16为true，可以加快计算速度
reranker = FlagReranker('BAAI_bge-reranker-large', use_fp16=True)

pairs = [["发什么快递？", "发哪家快递？"], ["发什么快递？", "什么物流公司？"]]
# 计算多对文本间的相关性评分
scores = reranker.compute_score(sentence_pairs=pairs, normalize=True)
print(scores)
