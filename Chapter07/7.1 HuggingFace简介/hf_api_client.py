#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/12 11:39
# @Author  : yongjie.su
# @File    : hf_api_client.py
# @Software: PyCharm
from huggingface_hub.hf_api import HfApi, list_models

# huggingface_hub 官网获取token
token = "hf_osxxx"

hf_api = HfApi(token=token)
# 返回 Iterable
models = list_models()
for model in models:
    print(model)

print(hf_api.whoami())

# 列出所有模型
# for model in hf_api.list_models():
#     print(model)

# 列出所有数据集
# for dataset in hf_api.list_datasets():
#     print(dataset)

# 下载模型
repo_id = "2Noise/ChatTTS"
model_files = hf_api.list_repo_files(repo_id, repo_type='model')
for model_file in model_files:
    hf_api.hf_hub_download(repo_id=repo_id, filename=model_file, local_dir='./tmp')

# 下载数据
# repo_id = "HuggingFaceFW/fineweb-edu"
# data_files = hf_api.list_repo_files(repo_id, repo_type='dataset')
# for data_file in data_files:
#     hf_api.hf_hub_download(repo_id=repo_id, filename=data_file, local_dir='./tmp')
