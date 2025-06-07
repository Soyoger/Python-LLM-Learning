#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/6 09:16
# @Author  : yongjie.su
# @File    : 8.3.1  文档加载器.py
# @Software: PyCharm
# from langchain.document_loaders import TextLoader
# CSVLoader
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='./example_data.csv', encoding='utf-8')
data = loader.load()
print(data)

# PDFLoader
from langchain_community.document_loaders import PyPDFium2Loader

pdf_loader = PyPDFium2Loader(file_path="./pdf测试文档.pdf")
data = pdf_loader.load()
print(data)

from langchain_community.document_loaders import MathpixPDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader
from langchain_community.document_loaders import PDFMinerLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import PyPDFDirectoryLoader
