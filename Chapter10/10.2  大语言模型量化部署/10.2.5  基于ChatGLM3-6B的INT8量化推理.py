#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/27 14:24
# @Author  : yongjie.su
# @File    : 10.2.5  基于ChatGLM3-6B的INT8量化推理.py
# @Software: PyCharm
import torch
from transformers import AutoTokenizer, AutoModel

if torch.cuda.is_available():
    print("CUDA is available!")
else:
    print("CUDA is not available.")

chatglm_6b_path = "chatglm3-6b"

tokenizer = AutoTokenizer.from_pretrained(chatglm_6b_path, trust_remote_code=True)
with torch.no_grad():
    model = AutoModel.from_pretrained(
        chatglm_6b_path,
        trust_remote_code=True
    ).quantize(8).cuda()

model = model.eval()
prompt = f"""
        任务：回答下面问题。
        问题：中国的首都在哪儿？
        限制：只告诉我答案，无关内容都不需要。        
"""
response, history = model.chat(tokenizer, prompt, history=[])
print(response)
