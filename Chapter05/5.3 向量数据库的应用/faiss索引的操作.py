#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/5/26 21:22
# @Author  : yongjie.su
# @File    : faiss索引的操作.py
# @Software: PyCharm
import faiss

# 创建索引
dim = 128
params = "PCA80,Flat"
measure = faiss.METRIC_L2
index = faiss.index_factory(dim, params, measure)

# 索引写入文件
faiss.write_index(index, 'demo.index')

# 读取索引文件
index = faiss.read_index('demo.index')

# 克隆索引
index_clone = faiss.clone_index(index)

