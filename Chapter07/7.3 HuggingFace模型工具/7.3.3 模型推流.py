#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/26 22:49
# @Author  : yongjie.su
# @File    : 7.3.3 模型推流.py
# @Software: PyCharm
# 使用微调的模型进行推理
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")
model = AutoModelForSequenceClassification.from_pretrained(
    "./train/model"
)
# import torch
# model.load_state_dict(torch.load("model/pytorch_model.bin"))
texts = [
    "dr. goldberg offers everything i look for in a general practitioner. ",
    "It seems that his staff simply never answers the phone.  It usually takes 2 hours of repeated calling to get an answer.  Who has time for that or wants to deal with it?  I have run into this problem with many other doctors and I just don't get it.  You have office workers, you have patients with medical needs"
]
encoded_inputs = tokenizer(
    texts,
    padding="max_length",
    truncation=True,
    return_tensors='pt'
)
print(encoded_inputs)
outputs = model(**encoded_inputs)
labels = outputs['logits'].argmax(dim=1)
print(labels.numpy().tolist())
