#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/9 14:20
# @Author  : yongjie.su
# @File    : 9.3.3  使用API 接口微调.py
# @Software: PyCharm
# JSONL 数据
from openai import OpenAI

api_key = ""
client = OpenAI(api_key=api_key)

# 上传文件
data_file_path = "mydata.jsonl"
client.files.create(
    file=open(data_file_path, "rb"),
    purpose="fine-tune"
)

# 查看文件列表
client.files.list()

# 创建一个微调模型
file_id = "file-xxx"
client.fine_tuning.jobs.create(
    training_file=file_id,
    model="gpt-3.5-turbo",
    suffix="2024-07-10"
)

# 用户可以对微调job的操作
# 列出前5个job
client.fine_tuning.jobs.list(limit=5)

# 查询微调job的状态
fine_tuning_job_id = "ftjob-xxx"
client.fine_tuning.jobs.retrieve(fine_tuning_job_id)

# 取消一个微调job
client.fine_tuning.jobs.cancel(fine_tuning_job_id)

# 查询微调job的5个事件
client.fine_tuning.jobs.list_events(fine_tuning_job_id=fine_tuning_job_id, limit=5)

# 删除微调模型
model = "ft:gpt-3.5-turbo:demo:suffix:2024-07-10"
client.models.delete(model)

# 使用微调模型
model = "ft:gpt-3.5-turbo:demo:suffix:2024-07-10"
completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "你是一个虚拟助手。"},
        {"role": "user", "content": "您好。"}
    ]
)
print(completion.choices[0].message)
