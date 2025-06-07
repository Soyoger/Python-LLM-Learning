#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/25 11:35
# @Author  : yongjie.su
# @File    : 7.3.4 评估.py
# @Software: PyCharm

# https://huggingface.co/docs/datasets/how_to_metrics

# 数据集中的指标已弃用。
# from datasets import list_metrics
# metrics = list_metrics()
# print(metrics)

# 用于轻松评估机器学习模型和数据集的库。
import evaluate

accuracy = evaluate.load("accuracy")
print(accuracy.description)
print(accuracy.citation)

# 计算 All-in-one
result = accuracy.compute(references=[0, 1, 0, 1, 1], predictions=[1, 0, 0, 1, 1])
print(result)

# add
for ref, pred in zip([0, 1, 0, 1, 1], [1, 0, 0, 1, 1]):
    accuracy.add(references=ref, predictions=pred)
print(accuracy.compute())

# add_batch
for refs, preds in zip([[0, 1], [0, 1], [1]], [[1, 0], [0, 1], [1]]):
    accuracy.add_batch(references=refs, predictions=preds)
print(accuracy.compute())
