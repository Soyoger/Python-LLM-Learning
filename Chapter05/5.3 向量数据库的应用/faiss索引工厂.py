#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/5/26 13:24
# @Author  : yongjie.su
# @File    : faiss索引工厂.py
# @Software: PyCharm
import faiss

# 创建索引
dim = 128
params = "PCA80,Flat"
measure = faiss.METRIC_L2
index = faiss.index_factory(dim, params, measure)
