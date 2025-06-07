#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/29 23:01
# @Author  : yongjie.su
# @File    : 14.3.4  基于RAG混合检索的互动问答实现.py
# @Software: PyCharm

# 关键词检索
# kw_responses = query_by_keyword(question, size=5)
# 向量检索
# vec_responses = query_by_vector(question, k=5)

# RRF算法

def reciprocal_rank_fusion(datasets, doc, k=60):
    """
    RRF 算法
    datasets = {
    "query1": ['doc1', 'doc2', 'doc3'],
    "query2": ['doc2', 'doc3', 'doc4'],
    }
    :param datasets:
    :param doc:
    :param k:
    :return:
    """
    queries = list(datasets.keys())

    def result_func(q):
        return datasets[q]

    def rank_func(results, d):
        return results.index(d) + 1

    rank_score = 0.0
    for q in queries:
        results = result_func(q)
        if doc in results:
            rank = rank_func(results, doc)
            rank_score += 1.0 / (k + rank)
    return rank_score


kw_responses = ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']
vec_responses = ['doc2', 'doc3', 'doc5', 'doc6', 'doc7']
k = 60
datasets = {
    "kw": kw_responses,
    "vec": vec_responses
}

docs = []
for key, values in datasets.items():
    docs.extend(values)

scores = {}
for doc in docs:
    score = reciprocal_rank_fusion(datasets, doc, k=60)
    scores[doc] = score

sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
hit_text = sorted_scores[0][0] if len(sorted_scores) > 0 else None
print(hit_text)
