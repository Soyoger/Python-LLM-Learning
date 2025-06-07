#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/17 22:11
# @Author  : yongjie.su
# @File    : 7.2.2  数据集工具基本操作.py
# @Software: PyCharm
from datasets import load_dataset_builder

ds_builder = load_dataset_builder("hltcoe/weibo_ner", trust_remote_code=True)

# 查看数据集名称
print(ds_builder.info.dataset_name)

# 检查数据集描述
print(ds_builder.info.description)

# 检查数据集特征
print(ds_builder.info.features)

from datasets import load_dataset

# # 加载数据集
dataset = load_dataset("hltcoe/weibo_ner", trust_remote_code=True)
print(dataset)

from datasets import get_dataset_split_names

# 获取数据集拆分名称
print(get_dataset_split_names("hltcoe/weibo_ner", trust_remote_code=True))

# 加载分割集train
dataset = load_dataset("hltcoe/weibo_ner", split="train", trust_remote_code=True)
print(dataset)

# 保存到本地磁盘
dataset = load_dataset("hltcoe/weibo_ner", trust_remote_code=True, num_proc=8)
dataset.save_to_disk("./tmp/weibo_ner")

# 从本次磁盘加载数据集
from datasets import load_from_disk

dataset = load_from_disk("./tmp/weibo_ner")

# 选择train的数据集
dataset = load_dataset("hltcoe/weibo_ner", split="train", trust_remote_code=True)

# 选择train+test的数据集
dataset = load_dataset("hltcoe/weibo_ner", split="train+test", trust_remote_code=True)

# 按train的行获取数据集
dataset = load_dataset("hltcoe/weibo_ner", split="train[10:20]", trust_remote_code=True)

# 按train的百分比获取数据集
dataset = load_dataset("hltcoe/weibo_ner", split="train", trust_remote_code=True)

print(dataset[:1])

# 数据排序
print(f"排序前ID值：{dataset['id'][:10]}")
sorted_dataset = dataset.sort(column_names=['id'], reverse=True)
print(f"排序后ID值：{sorted_dataset['id'][:10]}")

# 数据打散
print(f"打散前ID值：{dataset['id'][:10]}")
shuffled_dataset = dataset.shuffle(seed=100, writer_batch_size=10000)
print(f"打散后ID值：{shuffled_dataset['id'][:10]}")

# 按照下标对数据抽样
sample_dataset = dataset.select([0, 10, 20, 30])
print(f"抽样的数据集ID值：{sample_dataset['id']}")

# 数据集过滤
filtered_dataset = dataset.filter(lambda x: int(x['id']) < 10)
print(f"过滤后的数据集ID值：{filtered_dataset['id']}")

# 数据集切分
train_test_dataset = dataset.train_test_split(test_size=0.3, writer_batch_size=10000)
print(f"原始数据大小：{dataset.shape}")
print(f"训练集大小：{train_test_dataset['train'].shape}")
print(f"测试集大小：{train_test_dataset['test'].shape}")

# 数据集分片
num_shards = 5
index = 0
shard_dataset = dataset.shard(num_shards=num_shards, index=index)
print(f"原始数据大小：{dataset.shape}")
print(f"第{index}份数据大小：{shard_dataset.shape}")

# 重命名列名称
print(f"原始数据的列名称: {dataset.column_names}")
rename_dataset = dataset.rename_column('id', 'my_id')
print(f"重命名后数据的列名称: {rename_dataset.column_names}")
renames_dataset = rename_dataset.rename_columns({"tokens": "my_tokens", "ner_tags": "my_ner_tags"})
print(f"重命名后数据的列名称: {renames_dataset.column_names}")

# 删除数据集列
print(f"原始数据的列名称: {dataset.column_names}")
remove_dataset = dataset.remove_columns(["id"])
print(f"删除id列后数据集的列名称: {remove_dataset.column_names}")


# map 批处理
def add_one_to_id(item):
    item['id'] = int(item['id']) + 1
    return item


print(f"原始数据的前10个id值: {dataset['id'][:10]}")
new_dataset = dataset.map(add_one_to_id)
print(f"处理后数据的前10个id值: {new_dataset['id'][:10]}")
