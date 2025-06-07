#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 14:29
# @Author  : yongjie.su
# @File    : 7.1.2  HuggingFace Hub客户端库.py
# @Software: PyCharm
from huggingface_hub import login

# huggingface_hub 官网获取token
token = "hf_osxxx"

# 登陆
login(token=token)

# from huggingface_hub import logout
# 退出
# logout()


from huggingface_hub import whoami

# 用户信息
user = whoami()
print(user)

from huggingface_hub import create_repo

# 创建资源
repo_id = "soyoger/test-model"
create_repo(repo_id, private=True, repo_type="model")

from huggingface_hub import delete_repo

# 删除资源
repo_id = "soyoger/test-model"
delete_repo(repo_id, repo_type="model")

from huggingface_hub import hf_hub_download

# 下载资源
repo_id = "moka-ai/m3e-base"
filename = "config.json"
hf_hub_download(
    repo_id=repo_id,
    filename=filename,
    repo_type="model",
    local_dir='./tmp'
)

from huggingface_hub import hf_hub_download, list_repo_files

# 下载完整的存储库
repo_id = "moka-ai/m3e-base"
model_files = list_repo_files(repo_id, repo_type='model')
for model_file in model_files:
    hf_hub_download(repo_id=repo_id, filename=model_file, local_dir='./tmp')

from huggingface_hub import snapshot_download

repo_id = "moka-ai/m3e-base"
snapshot_download(repo_id=repo_id, repo_type="model", local_dir='./tmp')

# 上传资源或文件
from huggingface_hub import upload_file

repo_id = "soyoger/test-model"
upload_file(
    path_or_fileobj="/path/README.md",
    path_in_repo="README.md",
    repo_id=repo_id,
    repo_type='model'
)
