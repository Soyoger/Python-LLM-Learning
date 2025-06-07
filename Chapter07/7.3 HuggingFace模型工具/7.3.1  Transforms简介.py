#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/19 11:06
# @Author  : yongjie.su
# @File    : 7.3.1  Transforms简介.py
# @Software: PyCharm

"""
    安装 transformers 库
    pip3 install transformers
"""

# 管道工具
# 首次使用会默认下载对应的模型，前提是科学上网
from typing import Dict, Any

from transformers import pipeline

# alias: sentiment-analysis
# 情感分析
# 指定task
# pipe = pipeline(task="text-classification", trust_remote_code=True)
# result = pipe("真的很好！")
# print(result)

# 指定model
# from transformers import pipeline
# pipe = pipeline(model="FacebookAI/roberta-large-mnli")
# result = pipe("good")
# print(result)

# 处理多个任务
# from transformers import pipeline
#
# pipe = pipeline(task="text-classification", trust_remote_code=True)
# result = pipe(["真的很好！", "速度太慢了", "非常好吃，推荐给大家！"])
# print(result)

# 使用迭代器
# import random
# from transformers import pipeline
#
# texts = ["真的很好！", "速度太慢了", "非常好吃，推荐给大家！"]
#
# pipe = pipeline(task="text-classification", trust_remote_code=True)
#
#
# def get_data():
#     while True:
#         # 假设每次随机取一个评论
#         data = random.choice(texts)
#         yield data
#
#
# for out in pipe(get_data()):
#     print(out)

# 批处理，如果有gpu 可以设置device
# import time
# from transformers import pipeline
#
# pipe = pipeline(task="text-classification", trust_remote_code=True)
#
# texts = ["真的很好！", "速度太慢了", "非常好吃，推荐给大家！"] * 10
# for batch_size in [1, 2, 4, 8]:
#     start = time.time()
#     for out in pipe(texts, batch_size=batch_size):
#         # print(out)
#         pass
#     end = time.time()
#     cost_time = end - start
#     print(f"{batch_size=}的耗时：{cost_time}")

# 自定义数据集
# import time
# from transformers import pipeline
# from torch.utils.data import Dataset
# from tqdm.auto import tqdm
#
#
# class MyDataset(Dataset):
#     def __len__(self):
#         return 5000
#
#     def __getitem__(self, i):
#         return "这是一条测试数据，可以替换成自己的数据项。"
#
#
# dataset = MyDataset()
#
# pipe = pipeline("text-classification")
# batch_sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
# cost_times = []
# for batch_size in batch_sizes:
#     print("-" * 50)
#     print(f"Streaming batch_size={batch_size}")
#     start = time.time()
#     for out in tqdm(pipe(dataset, batch_size=batch_size), total=len(dataset)):
#         # print(out)
#         pass
#     end = time.time()
#     cost_time = end - start
#     cost_times.append(cost_time)
#     print(f"{batch_size=}的耗时：{cost_time}")

# 绘制图
# import matplotlib.pylab as plt
# import matplotlib.font_manager as fm

# 加载字体
# font = fm.FontProperties(fname='./SimHei.ttf')
#
# plt.plot(batch_sizes, cost_times)
# # 添加标题和轴标签
# plt.title('BatchSize大小与推理时间统计图', fontproperties=font)
# plt.xlabel('x轴-batch_size大小', fontproperties=font)
# plt.ylabel('y轴-推理时间', fontproperties=font)
# plt.show()

# AutoClass工具

# 加载预先训练的标记器  AutoTokenizer
# from transformers import AutoTokenizer
#
# tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")
# sequence = "I love china."
# print(tokenizer(sequence))

# 加载预先训练的图像处理器 AutoImageProcessor
# from transformers import AutoImageProcessor
#
# image_processor = AutoImageProcessor.from_pretrained("google/vit-base-patch16-224")

# 加载预先训练的特征提取器  AutoFeatureExtractor
# from transformers import AutoFeatureExtractor
#
# feature_extractor = AutoFeatureExtractor.from_pretrained(
#     "ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition"
# )

# 加载预先训练的处理器  AutoProcessor
# from transformers import AutoProcessor
#
# processor = AutoProcessor.from_pretrained("microsoft/layoutlmv2-base-uncased")

# 加载预先训练的模型
# from transformers import AutoModelForSequenceClassification
#
# model = AutoModelForSequenceClassification.from_pretrained("distilbert/distilbert-base-uncased")
#
# from transformers import AutoModelForTokenClassification
#
# model = AutoModelForTokenClassification.from_pretrained("distilbert/distilbert-base-uncased")

# 文本生成 example
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2", trust_remote_code=True)

inputs = tokenizer(["An increasing sequence: one,"], return_tensors='pt')
print(inputs)
result = model.generate(**inputs, max_new_tokens=20, early_stopping=True)
print(result)
tokens = tokenizer.batch_decode(result)
print(tokens)
