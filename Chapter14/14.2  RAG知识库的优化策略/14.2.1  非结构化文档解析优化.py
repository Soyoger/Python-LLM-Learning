#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/25 21:04
# @Author  : yongjie.su
# @File    : 14.2.1  非结构化文档解析优化.py
# @Software: PyCharm
# CSV 解析器
from langchain.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(file_path='test.csv')
data = loader.load()

# PDF 解析器
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("test.pdf")
pages = loader.load_and_split()
