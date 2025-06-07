#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/9 14:27
# @Author  : yongjie.su
# @File    : ChatGPT 文件接口.py
# @Software: PyCharm
from openai import OpenAI

api_key = ""
client = OpenAI(api_key=api_key)

# 上传文件
upload_info = client.files.create(
    file=open("mydata.jsonl", "rb"),
    purpose="fine-tune"
)
print(upload_info)
# 返回值
# {
#   "id": "file-abc123",
#   "object": "file",
#   "bytes": 120000,
#   "created_at": 1677610602,
#   "filename": "mydata.jsonl",
#   "purpose": "fine-tune",
# }

# 文件列表
client.files.list()

# 检索文件
file_id = "file-abc123"
client.files.retrieve(file_id)

# 删除文件
file_id = "file-abc123"
client.files.delete(file_id)

# 检索文件内容
client.files.content("file-abc123")
