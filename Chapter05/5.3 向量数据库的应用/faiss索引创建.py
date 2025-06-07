#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/5/26 11:44
# @Author  : yongjie.su
# @File    : faiss索引创建.py
# @Software: PyCharm
import faiss
# d表示创建索引的维度
d = 64
# 创建一个FlatL2索引
faiss.IndexFlatL2(d)
