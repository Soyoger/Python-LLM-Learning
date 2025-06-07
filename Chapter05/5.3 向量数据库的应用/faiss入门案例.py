#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/5/13 22:54
# @Author  : yongjie.su
# @File    : faiss入门案例.py
# @Software: PyCharm
import faiss
import numpy as np

# 向量维度
d = 64
# index向量库的数据量
nb = 100000
# 待检索query的数目
nq = 10000
np.random.seed(1234)
xb = np.random.random((nb, d)).astype('float32')
# index向量库的向量
xb[:, 0] += np.arange(nb) / 1000.
xq = np.random.random((nq, d)).astype('float32')
xq[:, 0] += np.arange(nq) / 1000.

index = faiss.IndexFlatL2(d)
# 输出为True，代表该类index不需要训练，只需要add向量进去即可
print(index.is_trained)
# 将向量库中的向量加入到index中
index.add(xb)
# 输出index中包含的向量总数，为100000
print(index.ntotal)

# topK的K值
k = 4
# xq为待检索向量，返回的I为每个待检索query最相似TopK的索引list，D为其对应的距离
D, I = index.search(xq, k)
print(I[:5])
print(D[-5:])
