#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/20 14:13
# @Author  : yongjie.su
# @File    : 7.3.3 模型微调.py
# @Software: PyCharm
# 准备数据
from datasets import load_dataset

dataset = load_dataset("yelp_review_full")
print(dataset["train"][:2])

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")


def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)


tokenized_datasets = dataset.map(tokenize_function, batched=True)

small_train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(100))
small_eval_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(100))

# 训练
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(
    "google-bert/bert-base-cased",
    num_labels=5
)

from transformers import TrainingArguments

training_args = TrainingArguments(
    # 定义checkpoints 检查点路径
    output_dir="test_trainer",
    # 定义测试执行策略，值包括：no epoch steps
    evaluation_strategy='steps',
    # 定义每隔多少个step执行一次测试
    eval_steps=10,
    # 学习率
    learning_rate=1e-4,
    # 加入权重衰减，预防过拟合
    weight_decay=1e-2,
    # 是否使用GPU
    no_cuda=True,
    # 日志输出策略
    logging_strategy="steps",
    # 日志输出级别
    log_level="info"
)

import numpy as np
import evaluate

metric = evaluate.load("accuracy")


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)


from transformers import Trainer

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=small_train_dataset,
    eval_dataset=small_eval_dataset,
    compute_metrics=compute_metrics,
)

# 训练前评估
print("Evaluate")
# print(trainer.evaluate())

# 进行微调
print("Training")
print(trainer.train())

# 训练后评估
print("Evaluate")
print(trainer.evaluate())

# 模型保存
trainer.save_model(output_dir="./train/model")
